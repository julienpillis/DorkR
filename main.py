from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from urllib.parse import *

def get_results(driver,query,from_page = 1,to_page = 3,url = True, url_name = True,website_name = True, description = False, deep_info = False):
    """Retourne les résultats scrappés d'une requête"""

    # vérifications initiales et initialisation des variables
    if(from_page>to_page):to_page=from_page
    current_page=from_page
    end = False

    # création du dictionnaire à retourner
    infos = {}
    if (url): infos['url'] = []
    if (url_name): infos['url_name'] = []
    if (website_name): infos['website'] = []


    # boucle de scrapping
    while(current_page <= to_page and not end):

        url = "http://www.google.com/search?q=" + query + "&start=" + str((current_page - 1) * 10)
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        check = soup.find_all('div', class_="mnr-c")

        if(check==None) :
            end = True
        else:
            if(url or url_name):
                search_URL = soup.find_all('div', class_="yuRUbf")
                for h in search_URL:
                    link = h.a.get('href')
                    if (url):
                        infos['url'].append(link)
                    if (url_name):
                        infos['url_name'].append(h.h3.text)

            if(website_name):
                search_names = (soup.find_all('span', class_="VuuXrf"))
                for name in search_names:
                    infos['website'].append(name.text)

            current_page+=1

    return infos





def get_location(driver,url,country = True, region = False, city=False, ip = False):
    """ Retourne les informations relatives à la géolocalisation d'une URL"""

    infos = {}
    url_location = "https://check-host.net/ip-info?host=" + url

    driver.get(url_location)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    search_location = soup.find('table', class_="hostinfo result")
    row = search_location.tbody.find_all('tr')
    if(country) :
        try :
            infos["country"] = row[5].strong.text
        except :
            infos["country"] = None
    if(region):
        try :
            infos["region"] = (row[6].find_all('td'))[1].text
        except :
            infos["region"] = None
    if(city):
        try :
            infos["city"] = (row[7].find_all('td'))[1].text
        except :
            infos["city"] = None
    if (ip):
        try :
            infos["ip"] = row[0].strong.text
        except :
            infos["ip"] = None

    return infos




def generate_csv(dataFrame):
    """Génère un fichier csv à partir d'une liste des noms de colonnes et des observations associés"""
    return None





if __name__=="__main__":

    query = input("Saisir la requête : ")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    results = get_results(driver,query,from_page=1,to_page=-1,website_name=False,url_name=False)
    countries = []

    for res in results["url"] :
        print(urljoin(res, '/'))
        countries.append(get_location(driver,urljoin(res, '/'))["country"])

    d = pd.DataFrame()
    for key in results:
        d[key] = results[key]

    d["location"] = countries

    print(d)



