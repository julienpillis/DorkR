from bs4 import BeautifulSoup
import time
import pandas as pd
from urllib.parse import *
from tqdm import tqdm
from app import ask_pages


def get_location_params():
    """Returns the full list of position parameters that are possible."""
    return ["ip","country","city","region"]


def get_results_params():
    """Returns the full list of result parameters that are possible."""
    return ["url","url_name","short_url","description","deep_info"]


def get_results(driver,query,from_page = 1,to_page = 3,url_name = True,short_url = True, description = False, deep_info = False):
    """Get all scrapped results
    URL will be always scraped"""

    # initialization of useful variables
    start_page=from_page

    # initialization of the dictionary to return
    infos = {val : [] for val in get_results_params()}

    # scrapping loop

    for current_page in tqdm(range(start_page,to_page+1),desc="Scraping pages..."):
        url_to_explore = "http://www.google.com/search?q=" + query + "&start=" + str((current_page - 1) * 10)
        driver.get(url_to_explore)
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # checking if no result
        check = soup.find_all('div', class_="mnr-c")
        if(check==None) :
            break

        else:
            search_URL = soup.find_all('div', class_="yuRUbf")
            for h in search_URL:
                link = h.a.get('href')
                try :infos['url'].append(link)
                except : infos['url'].append("null")
                if (url_name):
                    try: infos['url_name'].append(h.h3.text)
                    except:
                        infos['url_name'].append("null")
                if (short_url):
                    try :infos['short_url'].append(urljoin(link, '/'))
                    except:infos['short_url'].append("null")

            current_page+=1

    # cleaning the dictionary from empty lists
    for key in infos.copy():
        if len(infos[key]) < 1:
            del infos[key]

    return infos


def get_location(driver, url, country = True, region = False, city=False, ip = False):
    """ Returns information about the geolocation of the URL"""

    infos = {val : [] for val in get_location_params()}
    url_location = "https://check-host.net/ip-info?host=" + url
    driver.get(url_location)
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # scrapping requested infos
    search_location = soup.find('table', class_="hostinfo result")
    if(search_location!=None):
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
    else :
        if country : infos["country"] = "null"
        if region : infos["region"] = "null"
        if city : infos["city"] = "null"
        if ip : infos["ip"] = "null"

    # cleaning the dictionary from empty lists
    for key in infos.copy():
        if len(infos[key]) < 1:
            del infos[key]

    return infos

def add_location(driver, results, country = True, region = False, city=False, ip = False):
    """Adding position to results"""

    location = {"country": [], "region": [], "city": [], "ip": []}
    for link in tqdm(results["url"],desc="Getting positions..."):
        pos = get_location(driver, urljoin(link, '/'), country, region, city, ip)
        for info in pos:
            location[info].append(pos[info])

    # cleaning the dictionary from empty lists
    for key in location.copy():
        if len(location[key]) < 1:
            del location[key]

    # adding positions to the dataFrame
    results.update(location)

def launch_scraping(driver,query,params,begin=-1,end=-1) :

    # Gerer les pages
    if(begin==-1):
        pages = ask_pages()
        begin = pages[0]
        end = pages[1]

    if len(params)>0:
        results = get_results(driver,query,from_page=begin,to_page=end,url_name="url_name" in params,short_url="short_url" in params)
    else :
        results = get_results(driver, query, from_page=begin, to_page=end) # default behavior

    if bool(set(params) & set(get_location_params())): # checking if we need to get position infos
        add_location(driver, results, ip ="ip" in params, country ="country" in params, region ="region" in params, city="city" in params)

    print("     Almost done, generating csv file...")
    generate_csv(pd.DataFrame.from_dict(results),query)


def generate_name(query):
    """Generates a file name from a query """
    query += " " + time.asctime()
    for c in r'[]/\;,><&*:%=+@!#^()|?^"~`]°¤\' ':
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


