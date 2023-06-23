# Dorking :  Exploration géographique de données sensibles



## Introduction

### Qu'est ce que le dorking ?
Le dorking représente des combinaisons (dorks) de mots-clés reconnus par les moteurs de recherche (des **opérateurs de recherche avancée**). Ces combinaisons sont utilisées afin d’affiner les critères de recherche. Ce procédé est équivalent à celui de **criblage** / filtrage antérieur à l’annonce des résultats de la requête 

En voici quelques exemples : 
* *site:fr abc* : récupérer les URLs ayant un TLD en .fr, et comportant la mention "abc"
* *filetype:pdf confidentiel* : récupérer les fichiers PDF contenant la mention "confidentiel"
* *intitle:finance filetype:xls* : récupérer les fichiers XLS dont le titre contient le mot "finance"

Actuellement, il existe 42 opérateurs de recherche pour le moteur de recherche de Google. Des opérateurs de recherche avancée existent également pour d'autres moteurs de recherche comme  BING , DuckDuckGo, Yahoo… mais sont moins nombreux. C'est pour cela que nous avons élaborer une méthodologie de collecte de données s'appuyant uniquement sur le moteur de Google. De plus, les résultats obtenus sont sensiblement identiques d'un moteur à l'autre.


![](https://md.picasoft.net/uploads/upload_a58d57f5306b4cc1bed1181a1220934c.png) <center>*Quelques opérateurs de recherche avancée pour le moteur de Google* ([*SpreadSecurity*](https://spreadsecurity.github.io/2016/07/18/information-gathering-with-google-search-engine.html))</center> 


### Dans quel contexte s'appuie l'analyse du dorking ?

Les technologies mettant en place le World Wide Web permettent la sur-prolifération de données au fil des années. Les données transitant dessus peuvent prendre n'importe quelle forme numérique (textuelles, visuelles, auditives) et sont d'origines très variées.

Chacune possède :
* une **une entité de référence**: données personnelles, données économiques, comptabilité nationale...
* provient d'un **provient d'un producteur et détenteur** de données :  laboratoires, administrations, entreprises, universités, utilisateur lambda...
* et ont subit des **opérations de collecte** et de mise en forme : mesure, codage, enquêtes, sondages, enregistrements...

Mais malheureusement, ces données, peu importe leur provenance, sont soumises aux aléas informatiques, et humains, et peuvent tomber entre les mains d'un utilisateur non autorisé.

:::info
C'est à partir de cette philosophie que l'utilité des dorks entre en jeu pour les utilisateurs malveillants. **Les dorks sont détounés** pour être utilisés dans la recherche de failles, de documents ou encore d'informations à accès normalement restreint .
:::


Il s'agit notamment d'un outil très populaire chez les attaquants durant la phase de repérage d’une attaque. 


:::warning
Le dorking s’accompagne donc de **responsabilités éthiques**. Comme vous l'aurez compris, la limite de cette pratique est le hacking malveillant. L’ objectif de cette collecte et de cette analyse n’est donc pas d’étudier le contenu de chacun des documents collectés, mais d'***étudier leur provenance, et déterminer quelles sont les principales cibles.***
:::


Le dorking est très facile à prendre en main, il ne nécessite pas de connaissance informatique particulière et est redoutablement efficace.

En voici quelques exemples : 

<p align="center" width="100%">
    <img width="50%" src="https://md.picasoft.net/uploads/upload_81057b9bc8e42f252b4b8af4711ecdf8.png">
    <img width="40%" src="https://md.picasoft.net/uploads/upload_f728c192c7f74cb52e54614392d2909b.png"> 
</p>

```
Requêtes utilisées :

filetype:xls "username | password" -form -template -sample -sheet1
filetype:doc inurl:"gov" intext:"default password is"
```

## Acquisition et production de données
### Méthodologie
Maintenant que le contexte de notre analyse a été introduit, nous pouvons regarder de plus près notre stratégie de collecte, de traitement, et d'analyse des données.

Pour ce faire, nous avons suivi le workflow suivant : 


![](https://md.picasoft.net/uploads/upload_d9eeb616a0124cf13bd2133037a7a985.png)


Au cours de cette partie, nous nous intéresserons à la construction de l'outil, au ciblage, à l'extraction et au traitement des données brutes.

La partie *Analyse* fera l'objet d'une partie spécifique.

### Elaboration d'un outil de scraping

L'objectif est de collecter les URLs résultantes d'une requête sur le moteur de recherche de Google. Pour cela, il existe déjà des outils de scraping tels que [Pagodo](https://github.com/opsdisk/pagodo). Cependant, cet outil ne permet pas d'effectuer du scraping sur une requête souhaitée, mais seulement sur celles de la [Google Hacking Database](https://www.exploit-db.com/google-hacking-database).
Le programme se met également en veille (60 minutes) lorsque Google détecte qu'il s'agit d'un robot et ce, malgré l'utilisation d'un proxy.

Ainsi, nous nous sommes naturellement mis à élaboré notre propre solution pour répondre aux besoins de ce projet et être plus rapides.


Pour cela, nous avons développé **DorkR**, un programme Python, utilisable sur terminal, capable de scraper (librairie **BeautifulSoup**) les URLs  d'une requête, que nous appellerons : *dork*.


___

![](https://md.picasoft.net/uploads/upload_07dda78c30a3689da1da8a4705effb29.png)
___

Il est capable d'effectuer un scraping sur une requête unique (commande *dork*), ou bien un ensemble de requêtes inscrit sur un fichier csv (commande *dork_csv*).
___


<center>
<p align="center" width="35%">
    <img width="35%" src="https://md.picasoft.net/uploads/upload_4e5f7917a85788554fcb24d04495c657.png"> 
</p>
</center>

<center> <i> Fonctionnement de l'outil </i> </center>

___


L'un des avantages non négligeables de cet outil est la possibilité de récupérer les informations relatives à la localisation d'une URL (du moins le lieu où elle est hébergée). Il est en mesure de collecte l'adresse IP, le pays, la région ou encore la ville. 

D'autres informations (secondaires) sont collectables telles que le nom de l'URL affiché par le moteur de recherche (*url_name*), une simplification de l'url (*short_url*) ou encore le Top Level Domain.

Il est également possible de préciser la portion de pages à scraper (indices des première et dernière pages). 


___


<center>
<p align="center" width="35%">
    <img width="85%" src="https://md.picasoft.net/uploads/upload_266d79c93b5dfcc60f99bd5c1f3bf2aa.png"> 
</p>
</center>

<center> <i> Génération du fichier .csv </i> </center>

___


A la fin de la phase de scraping, et éventuellement de la phase de récupération des informations de localisation, le programme génère un fichier .csv regroupant toutes les informations récoltées.

___


![](https://md.picasoft.net/uploads/upload_9ce218e7e00e7dd7a09691459e30ef5f.png)
<center> <i> Fichier .csv résultant </i> </center>

___


L'outil est malheureusement détectable par le moteur de recherche Google. Pour contourner ce problème, nous mettons le programme en pause et demandons à l'utilisateur de vérifier manuellement le CAPTCHA. Il faut donc être attentif au déroulement du programme, mais cela permet une reprise du scraping en seulement en quelques secondes.

> L'outil est disponible sur ce [lien](https://github.com/julienpillis/DorkR). Une version stable sera bientôt mise en ligne.

 

### Ciblage des requêtes

L'outil principal est maintenant développé et fonctionnel ! 

Nous pouvons désormais nous engager dans la phase de construction des requêtes et de collecte des données. Pour se faire, nous avons d'abord essayer à la main différentes requêtes et opérateurs et stocker les requêtes pertinentes dans le CSV qui suit. Pour agrandir notre base de requêtes, nous avons cherché des potentiels bases de requêtes déjà existante sur internet. Nous sommes notamment tombés sur la base [suivante](https://www.exploit-db.com/google-hacking-database), après avoir testé la pertinences des requêtes, nous les avons ajoutés à notre CSV suivant :

<iframe id="DorksList"
    title="List des requêtes"
    width="750"
    height="300"
    src="https://wwwetu.utc.fr/~pillisju/IC05/dorks_list.html">
</iframe>


On se retrouve au final avec un CSV de 155 requêtes, avec la répartition suivante : 
<center>
<p align="center">
    <img width="60%" src="https://md.picasoft.net/uploads/upload_4a5d858ed248d20b858266b2d2af6a91.png"> 
</p>
</center>

---
### Extraction

#### Collecte initiale
L'extraction des données s'est effectuée en trois phases. La première phase consistait à collecter les résultats des rêquetes que nous avions élaborées. Pour cela, il suffisait simplement d'utiliser DorkR, notre outil.

Sur cet ensemble de requêtes, nous avons obtenu environ 23 500 URLs.

#### Construction du réseau

La seconde phase sert à construire un réseau entre les URLs collectées, et les URLs vers lesquelles elles pointent. Ce réseau nous permettra, éventuellement, d'identifier des clusters d'URLs potentiellement sensibles, mais aussi de connaître les grands lieux de failles et d'intéressement de celles-ci.
Cela apporte également de nouvelles informations géographiques que nous étudierons dans la partie dédiée à l'analyse.

Les URLs peuvent cependant pointées vers des fichiers, et par conséquent, ne pas pointer vers d'autres URLs. Pour cela, nous avons décidé de les simplifier, en ne prenant en compte que la base de celle-ci.

Il existe déjà des outils comme **Hyphe** permettant de réaliser cela. Cependant, notre base d'URLs étant trop importante et l'outil Hyphe très lent, nous avons fait notre propre script pour collecter ce dont nous avions besoin. Ce script récupère uniquement les URLs d'une profondeur de 1 lien. 

Nous avons ainsi pu collecter 80 000 liens.

--- 

<center>
<p align="center" width="35%">
    <img width="85%" src="https://md.picasoft.net/uploads/upload_f2cca017f6395967c8cb771f03eddcfb.png"> 
</p>
</center>

<center> <i> Fichier .csv résultant </i> </center>


---

### Traitement


#### Catégorisation des TLDs

La troisième phase consistait à filtrer les TLDs des URLs scrapés afin d'effectuer par la suite des analyses plus pertinentes. Nous avons écrit un script permettant d'abord de raccourcir des tlds si ceux-ci sont en deux parties ou plus et de garder la partie la plus pertinente. (ex : gouv.fr --> gouv). Ce script permet ensuite de trier les TLDs en plusieurs catégories différentes : 
1. Government(gov, gouv, gob, mil...)
2. Education(edu, school, sch, ac...)
3. Health(health, med, care...)
4. Commerce(buy, eco, pay...)
5. Country(fr, us, uk, eu...)
6. Others(com, org, net, co...)

Le script est disponible sur ce [lien](https://github.com/julienpillis/DorkR/blob/Tools/process_tld.py), il permet notamment de voir les listes de tld des différentes catégories présentées.

#### Géolocalisation 

La dernière phase consistait à récuperer les coordonnées GPS des URLs. En effet, la ville n'est pas un élément suffisant pour pouvoir exploiter et localiser les URLs. Nous avons ainsi élaboré un script utilisant l'API **Nominatim**, permettant de collecter les coordonnées à partir de la ville. 

Les fichiers sont, sous ce format, exploitables par des outils de visualisation tels que **Gephi** ou certaines librairies R (**Plotly**, **MapBox**...)

---
![](https://md.picasoft.net/uploads/upload_9a64f37173f4b529825c89a1a6931e54.png)

<center> <i> Fichier .csv résultant pour la création du réseau</i> </center>

----

![](https://md.picasoft.net/uploads/upload_96f580ca3c93f366db6a5b55c58da3d2.png)

<center> <i> Fichier .csv résultant de la collecte initiale</i> </center>



---




### Les obstacles rencontrés

Bien évidemment, il n'a pas été aussi simple de récupérer ces résultats. Au cours du l'avancement, nous avons rencontré des difficultés qu'il a été parfois difficiles d'atténuer. 

![](https://md.picasoft.net/uploads/upload_4fcd30cd07e725884b7361fd7e78baa8.png)

Et notamment :

* déterminer zone de recherche
* évaluer la pertinence des requêtes
* évaluer la pertinence des résultats
* évaluer la représentativité des échantillons collectés

Ces quatre obstacles sont notamment survenus par une quantité trop faible de résultats collectés lors des premières tentatives d'extraction. Cela était dû à notre base de requêtes qui n'était pas assez fournie, et aux requêtes bien trop précises que nous avions développées. Nous ne pouvions pas assurer un représenativité des échantillons.

Par conséquent, nous avons dû étendre notre zone de recherche (variété des données collectées) et réduire la pertinence des résultats en réutilisant des requêtes (parfois peu pertinentes) de la [Google Hacking Database](https://www.exploit-db.com/google-hacking-database).

Nous avons tout de même évalué chaque requête que nous avons ajouté à notre base de données pour trouver le bon compris entre ces quatre obstacles. 




## Analyse

Dans cette partie, nous suivrons une démarche de rétro-ingenieurie dans l'analyse des données que nous avons collectées. Nous étudierons des éléments particuliers dans chaque partie, puis nous ferons une conclusion générale de l'analyse au sein de la partie *Conclusion* de ce rapport.

### Analyse géographique


En plançant géographiquement (à l'aide des coordonnées GPS) les liens entre les URLs collectées et les URLs vers lesquellent elles pointent, nous obtenons cette carte :

![world map](https://md.picasoft.net/uploads/upload_92a80f086e29cd51e24061cb3018e4c5.png)
<center>Réseau des URLs sources et cibles</center>

<p>
    
</p>

En effet, il n'est pas possible d'effectuer une analyse étant donné la grande quantité d'éléments que nous avons collectés ! 

Nous allons donc procéder à un découpage en couches, qui nous permettra de mieux distinguer les éléments caractéristiques de cette collecte.

Pour commencer, nous pouvons tracer la répartition, sous forme de nuage de points, des URLs collectées :




<iframe id="inlineFrameExample"
    title="Inline Frame Example"
    width="750"
    height="760"
    src="https://wwwetu.utc.fr/~pillisju/IC05/network_maps/source_pointscloud.html
">
</iframe>



Nous avons là une vision un peu plus claire et plus propre de notre jeu de données.

Regardons de plus près pour chacune de ces régions : 



<p align="center" width="100%">
    <img width="50%" src="https://md.picasoft.net/uploads/upload_cca14a1a6a96ac6ceefec9aa2cf3d311.png">
    <img width="40%" src="https://md.picasoft.net/uploads/upload_c2954c7e2f58f62ddf434942a60ebafd.png"> 
</p>
<p align="center" width="100%">
    <img width="50%" src="https://md.picasoft.net/uploads/upload_bb7aa73fb75ee0da45c564e355f58a67.png">
    <img width="40%" src="https://md.picasoft.net/uploads/upload_f13c7ef7ed2b82b57cc077553db22b21.png"> 
</p>

![Asie PO](https://md.picasoft.net/uploads/upload_0fe562d0b8616d9c2064f46fd6486531.png)

Nous apercevons plusieurs foyers de concentration ressortir : 
* L'Amérique du Nord
* Le Brésil
* L'Europe Centrale et l'Europe de l'Ouest
* Le Proche-Orient
* L'Afrique du Sud
* L'Inde
* L'Asie de l'Est (et notamment la Chine, le Japon et plus étonnant : l'Indonésie).


<center>
<p align="center" width="100%">
    <img width="100%" src="https://md.picasoft.net/uploads/upload_cd7e068e25bfdae78cdabf4432caf399.png"> 
</p>
    <p>
        <i> Répartition des URLs sources en % </i>
    </p>
</center>

Cependant, ces premières observations sont sans surprise. En effet, l'accès aux infrastructures numériques et au réseau Internet est très inégale selon les régions du monde. Se sont les pays développés et émergents (BRICS) qui bénéficient de la plus grande couverture réseau et d'un accès au monde numérique. 

<center>
<p align="center" width="80%">
    <img width="80%" src="https://md.picasoft.net/uploads/upload_3bd85c18506329643c8d93ac3e33a5ee.png"> 
</p>
    <p>
        Couverture réseau (fibre optique en bleu) et densité de population 
    </p>
    <p>
        <a href=https://bbmaps.itu.int/bbmaps>International Communication Union</a>
    </p>
</center>



Ces écarts, témoins directs des inégalités de richesse à travers le monde, apportent une certaine cohérence à nos données. Les foyers créateurs de contenus numériques sont logiquement ceux qui créent eux mêmes des failles informatiques et comprimissions de données visibles par dorking. Etant des pays riches, ils représentent donc des proies faciles pour la récupération de données personnelles et de potentielles cyber-attaques.

Cependant, remarquons également des disparités sur l'existence d'autorité nationale de la protection des données (voire même l'existence de loi, voir carte ci-dessous). L'ensemble des pays développés disposent d'une telle autorité, contrairement à d'autres régions du monde comme en Inde ou en Indonésie (malgré une importante couverture réseau). 

Ne s'agirait-il pas d'un paradoxe qui émergerait ? En effet, les lieux où la régulation des données semble être mieux encadrée, sont également les lieux produisant le plus de résultats par dorking.

Regardons donc de plus près de ce qu'il en est pour les pays n'ayant pas de loi ou de régulation aussi forte qu'au sein de l'U.E ou en Amérique du Nord.


<center>
<p align="center" width="80%">
    <img width="80%" src="https://md.picasoft.net/uploads/upload_ee566b6f6962e01c88d2eb951e2c6ae0.png"> 
</p>
    <p>
        Protection des données à travers le monde <a href=https://www.cnil.fr/en/data-protection-around-the-world>(CNIL)</a>
    </p>

</center>

:::    info
Les repères sont des autorités de réguation des données.
:::




#### Indonésie

Premièrement, il faut savoir que l'Indonésie est habité par 273,8 millions de personnes, ce qui en fait le 4ème pays le plus peuplé de la planète. Bénéficiant d'une bonne couverture réseau, le nombre d'utilisateurs est important et se classe parmi les 10 états ayant de le plus d'utilisateurs d'Internet (9ème position), pour une position de 16ème sur le classement par PIB.

<center>
<p align="center" width="80%">
    <img width="80%" src="https://md.picasoft.net/uploads/upload_0dcebf7fa357455340ade80723146d4b.png"> 
</p>
    <p>
        Liste des pays par nombre d'utilisateurs <a href=https://fr.wikipedia.org/wiki/Liste_de_pays_par_nombre_d%27utilisateurs_d%27Internet
>(Wikipédia)</a>
    </p>

</center>



Comme nous pouvons le remarquer, la position de l'Indonésie est assez confortable.

Malgrè tout, il faut savoir qu'elle ne dispose d'aucune loi (active) sur la Protection des Données Personnelles. En effet, ce n'est qu'en 2022 que la Chambre des Représentants de l'Indonésie a fait passé un telle loi. Cette loi n'entrera pas en vigueur avant octobre 2024.

Cette loi autorise la création d'une agence de régulation et s'accompagne de l'introduction de nouvelles infractions et délits relatives à la donnée.

Fortement inspirée de la RGPD, la loi offre aux individus la droit d'accès, de suppression et de modification de leurs données personnelles. 

Il est donc clair que cela marque un tournant dans l'histoire de la régulation des données en Indonésie. Autrefois, et encore aujourd'hui (jusqu'en 2024), aucune régulation sur la conservation et le partage de données n'est présente.

:::    success
Voici un article intéressant sur la régulation des données en Indonésie : 
- [Future of Privacy Forum, Data Protection Overview](https://fpf.org/blog/indonesias-personal-data-protection-bill-overview-key-takeaways-and-context/)

:::




#### L'Inde 

L'Inde se trouve dans une population similaire à l'Indonésie. Cependant, il s'agit du second pays utilisant le plus Internet (et par conséquent étant le plus sur le WEB). A ce jour, il n'existe pas réellement de loi concernant la protection des données personnelles bien qu'en 2017, la Cour suprême de l'Inde a reconnu le droit à la vie privée comme un droit fondamental. Elle a énoncé certains principes sur la confidentialité des informations. Le projet "Digital Data Protection Bill" était ambitieux : se rapprocher du RGPD.

Malheureusement, le projet n'a que peu évolué notamment à cause de l'article 35 introduit par le gouvernement : le gouvernement est exonéré de toutes les règles édictées s’il le juge nécessaire ou opportun dans l’intérêt de la souveraineté et de l’intégrité de l’Inde. 

Ainsi, ce sont les données de presque 400 000 000 d'utilisateurs, d'instances gouvernementales ou même d'entreprises qui sont exposées et soumises à aucune législation de protection forte. Mais ce sont aussi près de 900 000 000 de potentiels nouveaux utilisateurs qui peuvent se retrouver dans ce cas. D'autant plus que la population indienne est très variée et riche en informations : religions, castes, prestations sociales, numéros de téléphone, historique de consommation, transactions bancaires...


Ce projet a vu un nouvel élan en novembre 2022. Le ministère de l'Électronique et des Technologies de l'information a proposé une nouvelle proposition de loi de la Digital Data Protection Bill. Une fois adopté par le Parlement, il remplacerait les règles de 2011. Le projet de loi propose notamment d'introduire des obligations pour les entreprises (définies comme "Fiduciaires de données") qui déterminent les finalités et les moyens du traitement des données. Ce projet apporte en particulier plus de clarté pour fixer les responsabilités et la responsabilité en cas de violation des données personnelles




> Malrgé ces efforts, le face à face entre le gouvernement (voulant toujours garder la main sur les données) et l'opposition semble ralentir et alonger une nouvelle fois ce projet.

![](https://md.picasoft.net/uploads/upload_82b62450d0ea178d4ade4fff8957b987.png)
<p>
    <center><i>Répartition des catégories d'URLs du territoire en %</i></center>
</p>

On peut notamment voir sur la figure précédente qu'un nombre élevé de donnés proviennent directement d'instances publiques telles que le domaine de l'éducation et le gouvernement. Ces chiffres anormalement élevés traduisent sûrement le manque de législtations dans le pays à un point où même les données de ces instances sérieuses sont exposées. A titre de comparaison, pour les pays occidentaux, on arrive à un taux cumulés (gouvernement et éducation) maximum d'environ 15% contre plus de 40% ici.

:::    success
Voici quelques articles intéressants sur la régulation des données en Inde : 
- [France Culture, Guerre des données [Podacst] : Inde, l'impossible loi de protection ](https://www.radiofrance.fr/franceculture/podcasts/les-enjeux-des-reseaux-sociaux/guerre-des-donnees-4-4-l-inde-7917901)

- [Times of India, Digital Personal Data Protection Bill 2022](https://timesofindia.indiatimes.com/blogs/voices/digital-personal-data-protection-bill-2022-and-its-impact-on-indias-booming-data-centre-industry/) 
:::








#### Le Brésil

Le Brésil compose lui aussi une grande partie des utilisateurs d'Internet puisqu'il se trouve en 4ème position. Egalement 10 ème sur le classement du PIB nominal, et l'un des pays des BRICS, il se trouve tout comme les pays développés, en position de faiblaisse face aux cyberattaques et récolte de données.

En ce qui concerne la cybercriminalité et les violations de la vie privée, le Brésil est l'un des pays les plus touchés, non seulement en tant que cible mais aussi en tant que lieu d'origine. Au fil des années, le cybercrime brésilien s'est énormément développé : 


<center>
<p align="center" width="80%">
    <img width="75%" src="https://md.picasoft.net/uploads/upload_5e2b76dcd3a92412e07c680c0de8d475.png"> 
</p>
    <p> Le cybercrime au Brésil <a href=https://igarape.org.br/brazil-struggles-with-effective-cyber-crime-response>(Instituto Igarapé)</a>
    </p>

</center>



Il serait en réalité, son propre "ennemi".

L’apparaition dU RGPD en mai 2018 a incité les autorités brésiliennes à accélérer l’adoption de mesures lui permettant de s’intégrer au modèle européen et de lutter contre cette montée fulgurante de la cybercriminalité.

Seulement quelques mois après l'entrée en vigueur du RGPD (août 2018), la Loi Générale de Protection des Données Personnelles au Brésil est introduite au sein de la législation nationale. L'application de la loi a cependant pris effet eu lieu en 2020. 

La Loi porte principalement sur la collecte et le traitement des données personnelles et vise à garantir les éléments suivants :

* Réglementer la manière dont les entreprises et les organisations peuvent recueillir, utiliser et traiter les données à caractère personnel
* Compléter ou remplacer les lois fédérales sur la protection de la vie privée afin d'accroître la responsabilité des détenteurs des données
* Imposer des amendes aux entreprises et organisations qui ne respectent pas ses exigences
*  Permettre la **création d'une autorité chargée de la protection des données**
*  Imposer des règles sur le transfert des données à caractère personnel recueillies sur le territoire du Brésil


L'avancée par rapport à l'Inde et l'Indonésie est donc plus importante. Il reste cependant à voir si ces mesures seront réellement efficaces dans le temps.



:::    success
Voici quelques articles intéressants sur la régulation des données au Brésil : 
- [User Centrics, Brazil’s General Data Protection Law](https://usercentrics.com/knowledge-hub/brazil-lgpd-general-data-protection-law-overview/)

- [Blog du modérateur, LGPD](https://www.blogdumoderateur.com/lgpd-nouvelle-loi-bresilienne-protection-donnees-personnelles/) 
:::
#### La Chine

La Chine occupe la première place mondiale en termes d'utilisateurs connectés, ce qui en fait de loin le pays avec le plus grand nombre de données potentiellement exposées. Cependant, nous avons constaté que seulement environ 5% des URL proviennent de cette région. Cette disparité soulève plusieurs interrogations quant à son origine. Plusieurs raisons peuvent être identifiées pour expliquer cette situation.

* Depuis 2021, la Chine a mis en place une législation solide visant à renforcer la protection des données personnelles, en parallèle de l'établissement d'une agence de régulation dédiée. Cette loi vise à garantir plusieurs principes fondamentaux, tels que le consentement éclairé des individus, la transparence des entités collectant des données, ainsi que la sécurité renforcée des données privées. La loi PIPL(Personal Information Protection Law) est considérée comme une étape importante dans le renforcement de la protection des données personnelles en Chine. Elle s'inscrit dans un contexte plus large de réglementation stricte de la cybersécurité et de la gouvernance des données dans le pays. Cependant, il est encore trop tôt pour évaluer pleinement son impact et sa mise en œuvre pratique.

* La Chine a mis en place une censure et un contrôle stricts sur l'accès à l'Internet international, ce qui a conduit à l'émergence d'un "Great Firewall". Cela signifie que certains sites web et services en ligne populaires dans d'autres pays ne sont pas accessibles directement depuis la Chine, à moins d'utiliser des techniques de contournement. Le gouvernement chinois utilise diverses méthodes pour contrôler l'accès à l'Internet international. Cela comprend le blocage de sites web étrangers considérés comme politiquement sensibles ou contraires aux valeurs et aux politiques du gouvernement chinois. Les services de médias sociaux occidentaux, les plateformes de partage de vidéos et de nombreux sites d'information étrangers sont souvent inaccessibles en Chine.  Cependant, il est important de noter que bien que la Chine ait mis en place ces restrictions, de nombreux sites web et services chinois prospèrent à l'intérieur du pays, offrant un écosystème Internet dynamique et diversifié pour les utilisateurs chinois. Il convient également de mentionner que la Chine a développé son propre écosystème numérique avec des services en ligne populaires tels que WeChat, Alibaba, Baidu, Tencent, etc. Ces plateformes offrent une large gamme de services allant des médias sociaux aux achats en ligne, en passant par les paiements numériques, et sont utilisées par des centaines de millions de personnes en Chine.
* En raison des restrictions et de la censure en Chine, les utilisateurs chinois n'ont pas forcément accès à Google de la même manière que dans d'autres pays. Ils utilisent plutôt des moteurs de recherche locaux tels que Baidu, qui offrent des résultats de recherche adaptés à la langue et à la culture chinoises. Ces moteurs de recherche chinois sont devenus des acteurs majeurs sur le marché et proposent une gamme complète de services pour répondre aux besoins des utilisateurs chinois.

![](https://md.picasoft.net/uploads/upload_5457d856b5d0740bf5708074f2a0efa3.png)


:::    success
Voici un article intéressant sur la loi PIPL en Chine : 
- [Droit & Technologies](https://www.droit-technologie.org/actualites/entree-en-vigueur-de-la-pipl-le-rgpd-made-in-china/)
:::


#### Le futur du Royaume-Uni


Un cas intéressant est celui du Royaume-Uni. Le Brexit a marqué une nouvelle page pour ce territoire, et le domaine de la données et de la cybersécurité n'y a pas echappé.

Depuis le premier janvier 2022, le RGPD traditionnel a cessé d'avoir un effet direct au Royaume-Uni suite à la fin de la période de transition du Brexit (2020). Un projet de loi sur la protection des données personnelles et l’information numérique (Data Protection and Digital Information Bill) avait été introduit en juillet 2022 mais son examen avait été mis « en pause » avant même de démarrer.
 
L'objectif du gouvernement britannique est de conserver les meilleurs éléments de la RGPD (et en maintenir un niveau de protection équivalent à celui de l'UE), en abandonnant certaines limitations et obligations de reporting pour les entreprises. 

C'est alors que très récèmment, le 8 mars 2023, le gouvernement britannique a présenté une nouvelle version du projet de loi. Ce projet permettrait à l’économie britannique d’économiser plus de 4 milliards de livres sterling au cours des 10 prochaines années, tout en garantissant la protection de la vie privée et la sécurité des données personnelles.


Le DPDIB supprimera l'obligation pour les organisations qui ne mettent pas en œuvre de traitement à haut risque de créer et de conserver des enregistrements des activités de traitement. Mais cela ne les dégagera pas de l'obligation de veiller à ce que les données à caractère personnel soient traitées de manière licite, loyale et transparente. De plus, en pratique, toute organisation qui décide de renoncer au registre court le risque d'affecter la capacité des personnes concernées à répondre aux demandes d'accès, ou leur capacité à comprendre et à atténuer l'impact de toute violation de données personnelles ou cyberattaque.


Cette souplesse du traitement des données est source de nombreux débats et les avis divergents. En effet, il est légitime de se demander si ce "laisser-aller" n'ouvrirait pas des portes vers de potentielles cyberattaques, déjà bien présentes et notamment auprès des grandes universités. 


:::    success
Voici un article intéressant sur la régulation des données au Royaume-Uni : 
- [Squire Patton Boggs](https://larevue.squirepattonboggs.com/le-nouveau-projet-de-loi-britannique-sur-la-protection-des-donnees-reforme-de-bon-sens-ou-divergence-importante.html)
:::




### Analyse de réseau

Maintenant que nous avons étudiez la géographiquement nos résultats, nous pouvons ensuite s'intéresser au réseau.

![](https://md.picasoft.net/uploads/upload_c63487e10247db99589f75587608bb20.png)


<center>
<p align="center" width="40%">
    <img width="45%" src="https://md.picasoft.net/uploads/upload_b51739e46b67783d8f54a85f34f7fc05.png"> 
</p>
    <p> Légende des couleurs des noeuds
    </p>

</center>


(Ce graphe est le fruit d'un filtrage, parmi lequel nous avons supprimé les plus gros noeuds tels que Facebook, Instagram, Google... afin de soutirer des informations plus intéressantes.)

Si vous souhaitez parcourir parmis les liens que nous avons pu établir entre les URLs, vous pouvez intéragir avec la carte ci-dessous : 

<iframe id="inlineFrameExample"
    title="Inline Frame Example"
    width="750"
    height="600"
    src="https://wwwetu.utc.fr/~pillisju/IC05/network/">
</iframe>



Nous ne pouvons pas étudier ce graphe, qui est beaucoup trop conséquent. Nous allons donc procéder à un nettoyage et nous intéresser à la représentation des noeuds, en fonction de leur degré entrant. Les noeuds de degré entrant inférieur ou égal à 2 ont été également supprimés.

 Voici le résultat obtenu :
![](https://md.picasoft.net/uploads/upload_d87800efa6082b221c620dcf7098a86c.png)


Ce graphe est intéressant car est marqueur de nombreux clusters ! Regardons-les de plus près, et essayons de les comprendre.


#### Cluster : Technologies et informatique



![](https://md.picasoft.net/uploads/upload_07054c751b3550890983b2a675510c41.png)

**Observation :**

Il s'agit du cluster le plus visible. Nous y retrouvons de nombreux acteurs de la communauté technologique et informatique tels que : 
* Github
* Gitlab
* Reddit
* AskUbuntu
* PostFixAdmin
* StackOverflow
* Blackboard 
* Wordpress
* ...

La taille des noeuds (degré entrant) est modérée mais reste supérieure à la moyenne de la taille des noeuds du graphe.
Le nombre de liens entre les noeuds du cluster semble lui aussi être supérieur à la moyenne.


:::warning
:warning:  Les clusters ne regroupent pas la totalité des noeuds caractéristiques à ces clusters. On retrouve plusieurs autres points de concentration de noeuds de même "catégorie" mais dispersés dans le graphe.

<center>
<p align="center" width="40%">
    <img width="45%" src="https://md.picasoft.net/uploads/upload_676237dc2f6b90786a855a10dc9a361a.png"> 
</p>
    <p> Exemple de micro-cluster isolé du cluster T&IT
    </p>

</center>

:::

**Interprétation :**

En réalité, plusieurs causes peuvent expliquer la présence d'un tel cluster : 

* Partage de connaissance : De nombreux forums sont présents.  Comme nous l'avons énoncé en introduction, le dorking est une discipline de la cybersécurité. Les personnes intéréssées échangent sur ce sujet, et il se peut que nos résultats soient confondus par des exemples de dorking en provenance de ces forums ou même de sites éducatifs.


* Données non sécurisées par l'utilisateur :  De nombreuses platformes comme des sites WordPress, des projets GitLab, GitHub, PostFixAdmin... sont parfois manipulés par des utilisateurs non informaticiens, et par conséquent, non avertis des principes de sécurisations des systèmes. Il est alors possible que des identifiants, mots de passe ou encore failles classiques et connues soient retrouvables par dorking.

* Dépôts publics de code  : Comme énoncé précédemment Gitlab, Github ou autres dépôts de code sont des sources de failles assez courantes. Il arrive parfois que, dans le cas où les données ont été sécurisées par un utilisateur averti, ce soit le code lui même qui contiennent des failles. Il est alors simple de retrouver ces failles à l'aide d'un moteur de recherche.


#### Cluster : Etats-Unis

![](https://md.picasoft.net/uploads/upload_d06dec55b98bf2b0eaabee0e30b703f5.png)


**Observation :**

Présence faible de liens mais nombre assez important de noeuds.

**Interprétation :**

* Documents sensibles : Nous pouvons retrouver des documents anciennement classés confidentiel, des données personnelles relatives à des individus (adresse, adresse mail, numéro de téléphone), des descriptifs (intégrant par exemple des mots de passe par défaut pour l'utilisation de systèmes informatiques)...

* Simples redirections : Si un site gouvernemental a été cibié par une requête, il est très probable qu'il fasse des référence à d'autres sites gouvernementaux.

* C'est un témoin clair de la forte présence des résultats américains dans nos requêtes, et du potentiel d'éléments sensibles mis à disposition par ces sites/documents.


#### Cluster : Réseaux Sociaux et médias
![](https://md.picasoft.net/uploads/upload_a4966a90b58a7b7ff1715178ed0d4eed.png)


**Observation :**

Les principaux réseaux sociaux sont présents : 
* Telegram
* VK
* Discord
* Whatsapp
* Twitter
* Snapchat
* Instagram
* Linkedin
* Facebook
* ...

La taille des noeuds (degré entrant) est modérée mais reste supérieure à la moyenne de la taille des noeuds du graphe.
Le nombre de liens entre les noeuds du cluster semble lui aussi être supérieur à la moyenne.

**Interprétation :**
* Données non sécurisées par l'utilisateur : L'ensemble des réseaux sociaux sont des sources de données. Ils arrivent parfois que des utilisateurs partagent des données personnelles telles que leur adresse, numéro de téléphone ou encore adresse e-mail. Ces éléments sont très facilement retrouvables par dorking. Des dépôts de documents comme Issuu sont également concernés par ces problèmes humains.
* Partage de connaissance : De la même façon que le cluster Technologie et Informatique, le partage de connaissance s'effectue beaucoup par les réseaux sociaux et en particulier Discord, Youtube voire même LinkedIn, et peuvent marquer l'interêt de certains individus autour de ce sujet.
* Simples redirections vers les comptes de l'entité (la plus probable) : Il peut tout simplement s'agir d'effets de bords. Il est très fréquent que les entités renvoient vers leurs comptes de réseaux sociaux depuis leur site web.


#### Cluster : International
![](https://md.picasoft.net/uploads/upload_f64220ece46aca1fbef5330be32888a4.png)

**Observation :**

Aucun lien et noeuds de faibles importance.


**Interprétation :**
* Données non sécurisées par l'utilisateur : Il se peut que les URLs récupérées par dorking contiennent des failles web ou bien des données personnelles comme des mots de passes. Les urls peuvent pointer vers de nouvelles pages du site principal.
* Redirection vers un site gouvernemental : Si un site gouvernemental a été ciblé par une requête, il est très probable qu'il fasse des référence à d'autres sites gouvernementaux.





## Conclusion 

Pour terminer cette étude, nous vous proposons une brève conclusion récapitulant et inteprétant nos observations.

Théoriquement, nous savons que les pays développés ont généralement une meilleure régulation et une plus grande sensibilisation à la protection des données. Le cas des pays émergents est un peu plus complexe. Certains pays sont en train de mettre en place des lois pour combler ce vide, tandis que d'autres (par exemple : l'Inde) semble au point mort.

Les disparités que nous avons observées sont encore importantes à l'échelle mondiale. La sensibilisation et la régulation de la protection des données restent des enjeux cruciaux pour assurer la sécurité et la confidentialité des informations personnelles dans un monde de plus en plus connecté.

Cependant, un paradoxe est mis en évidence dans cette étude. Plus un territoire est important (économiquement et en nombre d'individus) et développé sur le plan numérique, plus il peut être exposé aux dangers liés à la protection des données. Les pays développés  qui bénéficient d'infrastructures numériques avancées et d'un accès à Internet plus large sont souvent les cibles privilégiées des cyberattaques et de la récupération de données personnelles, malgré la présence d'autorités de régulation et de lois. Cela s'explique en partie par le fait que ces pays produisent et créent une quantité importante de données, ce qui les rend vulnérables aux failles de sécurité et aux compromissions de données. 

De son côté, l'analyse du réseau met en évidence la présence de plusieurs clusters distincts, reflétant différentes catégories d'entités et de thématiques. Chacun de ces clusters présente des caractéristiques spécifiques et peut être interprété à travers diverses perspectives. Ils marquent également la diversité des origines des URLs que nous avons scrapées, et témoignent ainsi de l'étendu du "problème" du dorking dans ces systèmes très différents (sites gouvernementaux, dépôts de code, sites personnels...)

Dans l'ensemble, ce graphe souligne les défis liés à la sécurité des données et à la protection de la vie privée dans différents domaines. Il met en évidence l'importance d'une sensibilisation accrue à la sécurité informatique et à la protection des données, aussi bien pour les utilisateurs non informaticiens que pour les développeurs.

En outre, il souligne la nécessité de renforcer les mesures de sécurité dans les domaines de la technologie, des réseaux sociaux, et même au niveau international, afin de minimiser les risques liés à la divulgation d'informations sensibles.


