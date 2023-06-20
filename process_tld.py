import pandas as pd
import time

national_tlds = [
        "ad",  # Andorra
        "ae",  # United Arab Emirates
        "af",  # Afghanistan
        "ag",  # Antigua and Barbuda
        "ai",  # Anguilla
        "al",  # Albania
        "am",  # Armenia
        "an",  # Netherlands Antilles (Discontinued)
        "ao",  # Angola
        "aq",  # Antarctica
        "ar",  # Argentina
        "as",  # American Samoa
        "at",  # Austria
        "au",  # Australia
        "aw",  # Aruba
        "ax",  # Åland Islands
        "az",  # Azerbaijan
        "ba",  # Bosnia and Herzegovina
        "bb",  # Barbados
        "bd",  # Bangladesh
        "be",  # Belgium
        "bf",  # Burkina Faso
        "bg",  # Bulgaria
        "bh",  # Bahrain
        "bi",  # Burundi
        "bj",  # Benin
        "bl",  # Saint Barthélemy
        "bm",  # Bermuda
        "bn",  # Brunei Darussalam
        "bo",  # Bolivia
        "bq",  # Bonaire, Sint Eustatius and Saba
        "br",  # Brazil
        "bs",  # Bahamas
        "bt",  # Bhutan
        "bv",  # Bouvet Island
        "bw",  # Botswana
        "by",  # Belarus
        "bz",  # Belize
        "ca",  # Canada
        "cc",  # Cocos (Keeling) Islands
        "cd",  # Democratic Republic of the Congo
        "cf",  # Central African Republic
        "cg",  # Republic of the Congo
        "ch",  # Switzerland
        "ci",  # Côte d'Ivoire
        "ck",  # Cook Islands
        "cl",  # Chile
        "cm",  # Cameroon
        "cn",  # China
        "cr",  # Costa Rica
        "cu",  # Cuba
        "cv",  # Cape Verde
        "cw",  # Curaçao
        "cx",  # Christmas Island
        "cy",  # Cyprus
        "cz",  # Czech Republic
        "de",  # Germany
        "dj",  # Djibouti
        "dk",  # Denmark
        "dm",  # Dominica
        "do",  # Dominican Republic
        "dz",  # Algeria
        "ec",  # Ecuador
        "ee",  # Estonia
        "eg",  # Egypt
        "er",  # Eritrea
        "es",  # Spain
        "et",  # Ethiopia
        "eu",  # European Union
        "fi",  # Finland
        "fj",  # Fiji
        "fk",  # Falkland Islands (Malvinas)
        "fm",  # Federated States of Micronesia
        "fo",  # Faroe Islands
        "fr",  # France
        "ga",  # Gabon
        "gb",  # United Kingdom
        "gd",  # Grenada
        "ge",  # Georgia
        "gf",  # French Guiana
        "gg",  # Guernsey
        "gh",  # Ghana
        "gi",  # Gibraltar
        "gl",  # Greenland
        "gm",  # Gambia
        "gn",  # Guinea
        "gp",  # Guadeloupe
        "gq",  # Equatorial Guinea
        "gr",  # Greece
        "gs",  # South Georgia and the South Sandwich Islands
        "gt",  # Guatemala
        "gu",  # Guam
        "gw",  # Guinea-Bissau
        "gy",  # Guyana
        "hk",  # Hong Kong
        "hm",  # Heard Island and McDonald Islands
        "hn",  # Honduras
        "hr",  # Croatia
        "ht",  # Haiti
        "hu",  # Hungary
        "id",  # Indonesia
        "ie",  # Ireland
        "il",  # Israel
        "im",  # Isle of Man
        "in",  # India
        "io",  # British Indian Ocean Territory
        "iq",  # Iraq
        "ir",  # Iran
        "is",  # Iceland
        "it",  # Italy
        "je",  # Jersey
        "jm",  # Jamaica
        "jo",  # Jordan
        "jp",  # Japan
        "ke",  # Kenya
        "kg",  # Kyrgyzstan
        "ki",  # Kiribati
        "km",  # Comoros
        "kn",  # Saint Kitts and Nevis
        "kp",  # North Korea
        "kr",  # South Korea
        "kw",  # Kuwait
        "ky",  # Cayman Islands
        "kz",  # Kazakhstan
        "la",  # Laos
        "lb",  # Lebanon
        "lc",  # Saint Lucia
        "li",  # Liechtenstein
        "lk",  # Sri Lanka
        "lr",  # Liberia
        "ls",  # Lesotho
        "lt",  # Lithuania
        "lu",  # Luxembourg
        "lv",  # Latvia
        "ly",  # Libya
        "ma",  # Morocco
        "mc",  # Monaco
        "md",  # Moldova
        "me",  # Montenegro
        "mf",  # Saint Martin (French part)
        "mg",  # Madagascar
        "mh",  # Marshall Islands
        "mk",  # North Macedonia
        "ml",  # Mali
        "mm",  # Myanmar
        "mn",  # Mongolia
        "mo",  # Macau
        "mp",  # Northern Mariana Islands
        "mq",  # Martinique
        "mr",  # Mauritania
        "ms",  # Montserrat
        "mt",  # Malta
        "mu",  # Mauritius
        "mv",  # Maldives
        "mw",  # Malawi
        "mx",  # Mexico
        "my",  # Malaysia
        "mz",  # Mozambique
        "na",  # Namibia
        "nc",  # New Caledonia
        "ne",  # Niger
        "nf",  # Norfolk Island
        "ng",  # Nigeria
        "ni",  # Nicaragua
        "nl",  # Netherlands
        "no",  # Norway
        "np",  # Nepal
        "nr",  # Nauru
        "nu",  # Niue
        "nz",  # New Zealand
        "om",  # Oman
        "pa",  # Panama
        "pe",  # Peru
        "pf",  # French Polynesia
        "pg",  # Papua New Guinea
        "ph",  # Philippines
        "pk",  # Pakistan
        "pl",  # Poland
        "pm",  # Saint Pierre and Miquelon
        "pn",  # Pitcairn
        "pr",  # Puerto Rico
        "ps",  # State of Palestine
        "pt",  # Portugal
        "pw",  # Palau
        "py",  # Paraguay
        "qa",  # Qatar
        "re",  # Réunion
        "ro",  # Romania
        "rs",  # Serbia
        "ru",  # Russia
        "rw",  # Rwanda
        "sa",  # Saudi Arabia
        "sb",  # Solomon Islands
        "sc",  # Seychelles
        "sd",  # Sudan
        "se",  # Sweden
        "sg",  # Singapore
        "sh",  # Saint Helena, Ascension and Tristan da Cunha
        "si",  # Slovenia
        "sj",  # Svalbard and Jan Mayen
        "sk",  # Slovakia
        "sl",  # Sierra Leone
        "sm",  # San Marino
        "sn",  # Senegal
        "so",  # Somalia
        "sr",  # Suriname
        "ss",  # South Sudan
        "st",  # Sao Tome and Principe
        "sv",  # El Salvador
        "sx",  # Sint Maarten (Dutch part)
        "sy",  # Syria
        "sz",  # Eswatini
        "tc",  # Turks and Caicos Islands
        "td",  # Chad
        "tf",  # French Southern Territories
        "tg",  # Togo
        "th",  # Thailand
        "tj",  # Tajikistan
        "tk",  # Tokelau
        "tl",  # Timor-Leste
        "tm",  # Turkmenistan
        "tn",  # Tunisia
        "to",  # Tonga
        "tr",  # Turkey
        "tt",  # Trinidad and Tobago
        "tv",  # Tuvalu
        "tw",  # Taiwan
        "tz",  # Tanzania
        "ua",  # Ukraine
        "ug",  # Uganda
        "uk",  # United Kingdom
        "us",  # United States
        "uy",  # Uruguay
        "uz",  # Uzbekistan
        "va",  # Vatican City
        "vc",  # Saint Vincent and the Grenadines
        "ve",  # Venezuela
        "vg",  # British Virgin Islands
        "vi",  # U.S. Virgin Islands
        "vn",  # Vietnam
        "vu",  # Vanuatu
        "wf",  # Wallis and Futuna
        "ws",  # Samoa
        "ye",  # Yemen
        "yt",  # Mayotte
        "za",  # South Africa
        "zm",  # Zambia
        "zw"  # Zimbabwe
    ]
tlds_education = ['edu', 'ac', 'school', 'university', 'college', 'academy', 'education','learning', 'courses', 'institute', 'study', 'schule', 'mba', 'degree', 'shiksha', 'museum', 'prof', 'sch']
tlds_gov = ['tax', 'army', 'airforce', 'republican', 'vote', 'democrat', 'voto', 'voting', 'navy', 'int', 'gov', 'gop', 'post', 'mil', '政府', '政务', 'gob', 'gouv', 'mil', 'gop']
tlds_health = ['skin', 'med', 'pharmacy', 'dds','dentist', 'dental', 'rehab', 'surgery', 'diet', 'health', 'hospital', 'physio', 'hiv', 'fitness', 'vet', 'rip', 'care', 'doctor', 'vision', 'clinic', 'fit', 'healthcare']
tlds_money = ['coop', '商店', 'بازار', 'free', '购物', '网店', '商城', 'buy', 'deal', 'セール', 'ストア', 'save', 'coupon', '通販','gives', 'gratis', 'creditcard', 'discount', 'feedback', 'tienda', 'eco', 'gifts', 'qpon', 'kaufen','bargains', 'coupons', 'direct', 'blackfriday', 'guide', 'gift', 'promo', 'forsale', 'deals', 'shopping','store', 'bid', 'review', 'sale', 'cheap', 'reviews', 'cash', 'report', 'auction', 'kaufen', 'bank', 'broker', 'cfd', 'trading', 'markets', 'forex', 'spreadbetting', 'insurance', 'versicherung', 'free', 'lotto', 'pay', 'creditunion', 'buy', 'lifeinsurance', 'gratis', 'creditcard', 'discount', 'green', 'holdings', 'lease', 'eco', 'loans', 'rich', 'insure', 'ventures', 'credit', 'investments', 'fund', 'financial', 'estate', 'tax', 'exchange', 'claims', 'mortgage', 'trade', 'market', 'money', 'finance', 'marketing', 'cheap', 'cash', 'gold', 'capital', 'loan']
other_tlds = ['co', 'com']


def process_tlds(filename):

    list_tlds = tlds_gov + tlds_education + tlds_health + tlds_money + national_tlds + other_tlds

    #simplify tlds
    queries = pd.read_csv(f"{filename}.csv", header=0 ,sep=';')
    tlds = queries["tld"]
    tlds_clean = []
    i = 2
    for tld in tlds :
        if pd.notnull(tld) :
            tld_clean = simplify_tld(tld, list_tlds)
            tlds_clean.append(tld_clean)
        else : tlds_clean.append('')
        i+=1

    queries['tld_clean'] = tlds_clean

    #categorize tld
    tlds = queries["tld_clean"]
    tlds_cat=[]
    for tld in tlds:
        if pd.notnull(tld):
            tld_cat = categorize_tld(tld)
            tlds_cat.append(tld_cat)
        else:
            tlds_cat.append('')
        i += 1

    queries['tld_category'] = tlds_cat

    #Get URL's region
    latitudes = queries["Latitude"]
    longitudes = queries["Longitude"]
    Region = []
    for i in range(len(latitudes)):
        if pd.notnull(latitudes[i]) and pd.notnull(longitudes[i]):
            Region.append(determine_region(latitudes[i], longitudes[i]))
        else:
            Region.append('')

    queries['Region'] = Region

    #create new csv
    name = "clean_tld_" + time.asctime()
    for c in r'[]/\;,><&*:%=+@!#^()|?^"~`]°¤\' ':
        name = name.replace(c, '_')

    queries.to_csv(f"merge_clean.csv", sep=';', encoding='utf-8', index=False)

#simplify tld
#prioritized_tld_list sorted from highest to lowest known tld priority
def simplify_tld(tld, prioritized_tld_list):
    #print("TLD processed :", tld)
    tld = tld.lower()
    if '.' not in tld:
        #print(tld, "single part, already simplified")
        return tld
    # first reference found of a "."
    point_index = tld.index('.')
    left_part = tld[:point_index]
    right_part = tld[point_index + 1:]
    if '.' not in right_part:
        if left_part in prioritized_tld_list:
            if right_part not in prioritized_tld_list:
                #print(left_part, "takes priority over ", right_part)
                return left_part
            else:
                index_left = prioritized_tld_list.index(left_part)
                index_right = prioritized_tld_list.index(right_part)
                if index_left >= index_right:
                    #print(right_part, "takes priority over ", left_part)
                    return right_part
                else:
                    #print(left_part, "takes priority over ", right_part)
                    return left_part
        elif right_part in prioritized_tld_list:
            if left_part not in prioritized_tld_list:
                #print(right_part, "takes priority over ", left_part)
                return right_part
            else:
                index_left = prioritized_tld_list.index(left_part)
                index_right = prioritized_tld_list.index(right_part)
                if index_right >= index_left:
                    #print(left_part, "takes priority over ", right_part)
                    return left_part
                else:
                    #print(right_part, "takes priority over ", left_part)
                    return right_part
        else:
            #print("no recognized tld, returns unchanged tld...")
            return right_part
    else:
        #print("Tld is in more than two parts, subprocessing...")
        point_index = right_part.index('.')
        left_part_tmp = right_part[:point_index]
        right_part_tmp = right_part[point_index + 1:]
        tmp = simplify_tld(left_part + "." + left_part_tmp, prioritized_tld_list)
        return simplify_tld(tmp + "." + right_part_tmp, prioritized_tld_list)

def categorize_tld(tld) :
    if tld in tlds_gov :
        return "government"
    elif tld in tlds_education :
        return "education"
    elif tld in tlds_health :
        return "health"
    elif tld in tlds_money :
        return "commerce"
    elif tld in national_tlds:
        return "country"
    else :
        return "others"

def determine_region(latitude, longitude):
    if 49.6 <= latitude <= 58.9 and -6.4 <= longitude <= 1.9:
        return "Angleterre"
    elif 35 <= latitude <= 71 and -24 <= longitude <= 40:
        return "Europe"
    elif 6 <= latitude <= 37 and 68 <= longitude <= 97:
        return "Inde"
    elif -11 <= latitude <= 6 and 94 <= longitude <= 141:
        return "Indonésie"
    elif 18 <= latitude <= 54 and 73 <= longitude <= 135:
        return "Chine"
    elif -34 <= latitude <= 6 and -74 <= longitude <= -34:
        return "Brésil"
    elif 7 <= latitude <= 83 and -168 <= longitude <= -59:
        return "Amérique du Nord"
    elif -10 <= latitude <= 65 and 25 <= longitude <= 179:
        return "Asie"
    else:
        return "Autres"



if __name__=="__main__":
    #file_name = "geo_Thu_May_18_21_58_48_2023_clean"
    #process_tlds(file_name)
    pass
