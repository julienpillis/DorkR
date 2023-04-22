from bs4 import BeautifulSoup
import time
import pandas as pd
from urllib.parse import *

def get_position_params():
    """Returns the full list of position parameters that are possible."""
    return ["ip","country","city","region"]


def get_results_params():
    """Returns the full list of result parameters that are possible."""
    return ["url","url_name","short_url","description","deep_info"]


def get_results(driver,query,from_page = 1,to_page = 3,url_name = True,short_url = True, description = False, deep_info = False):
    """Get all scrapped results"""

    # initialization of useful variables
    if(from_page>to_page):to_page=from_page
    current_page=from_page
    end = False

    # initialization of the dictionary to return
    infos = {val : [] for val in get_results_params()}


    # scrapping loop
    while(current_page <= to_page and not end):

        url = "http://www.google.com/search?q=" + query + "&start=" + str((current_page - 1) * 10)
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # checking if no result
        check = soup.find_all('div', class_="mnr-c")
        if(check==None) :
            end = True

        else:
            if(url or url_name):
                search_URL = soup.find_all('div', class_="yuRUbf")
                for h in search_URL:
                    link = h.a.get('href')
                    if (url):
                        try :
                            infos['url'].append(link)
                        except : infos['url'].append("null")
                    if (url_name):
                        try: infos['url_name'].append(h.h3.text)
                        except:
                            infos['url_name'].append("null")


            current_page+=1

    # cleaning the dictionary from empty lists
    for key in infos.copy():
        if len(infos[key]) < 1:
            del infos[key]

    return infos


def get_position(driver, url, country = True, region = False, city=False, ip = False):
    """ Returns information about the geolocation of the URL"""

    infos = {val : [] for val in get_position_params()}
    url_location = "https://check-host.net/ip-info?host=" + url
    driver.get(url_location)
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # scrapping requested infos
    search_location = soup.find('table', class_="hostinfo result")
    row = search_location.tbody.find_all('tr')
    if(country) :
        try :
            infos["country"] = row[5].strong.text
        except :
            infos["country"] = "null"
    if(region):
        try :
            infos["region"] = (row[6].find_all('td'))[1].text
        except :
            infos["region"] = "null"
    if(city):
        try :
            infos["city"] = (row[7].find_all('td'))[1].text
        except :
            infos["city"] = "null"
    if (ip):
        try :
            infos["ip"] = row[0].strong.text
        except :
            infos["ip"] = "null"

    # cleaning the dictionary from empty lists
    for key in infos.copy():
        if len(infos[key]) < 1:
            del infos[key]

    return infos

def add_position(driver,results, country = True, region = False, city=False, ip = False):
    """Adding position to results"""

    position = {"country": [], "region": [], "city": [], "ip": []}
    for link in results["url"]:
        pos = get_position(driver, urljoin(link, '/'), country,region, city, ip)
        for info in pos:
            position[info].append(pos[info])

    # cleaning the dictionary from empty lists
    for key in position.copy():
        if len(position[key]) < 1:
            del position[key]

    results.update(position)

def launch_scraping(driver,query,params) :
    # Gerer les pages
    print("     Scraping begins !")
    if len(params)>0:
        results = get_results(driver,query,from_page=1,to_page=-1,url_name="url_name" in params,short_url="short_url" in params)
    else :
        results = get_results(driver, query, from_page=1, to_page=-1) # default behavior

    if bool(set(params) & set(get_position_params())): # checking if we need to get position infos
        print("     Now getting positions !")
        add_position(driver,results,ip = "ip" in params,country = "country" in params,region = "region" in params,city="city" in params)

    print("     Almost done, generating csv file...")
    generate_csv(pd.DataFrame.from_dict(results),query)


def generate_name(query):
    """Generates a file name from a query """
    query += " " + time.asctime()
    for c in r'[]/\;,><&*:%=+@!#^()|?^ ':
        query = query.replace(c, '_')
    return query

def generate_csv(dataFrame,query):
    """Generates a csv file from a query and its dataFrame"""
    name = generate_name(query)
    try:
        dataFrame.to_csv (f'{name}.csv', index = None, header=True,encoding="utf-8-sig")
        print(f"     \033[1m{name}.csv\033[0m has been successfully generated.")
    except :
        print("     An error occured during the csv generation.")

