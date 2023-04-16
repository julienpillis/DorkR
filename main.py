from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

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
    while(not end):

        url = "http://www.google.com/search?q=" + query + "&start=" + str((current_page - 1) * 10)
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        check = soup.find_all('div', class_="mnr-c")
        if(check==None) :
            end = True
        else :
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

            # vérification si arrêt imposé
            if(to_page!=-1) :
               end = current_page <= to_page
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
        infos["country"] = row[5].strong.text
    if(region):
        infos["region"] = (row[6].find_all('td'))[1].text
    if(city):
        infos["city"] = (row[7].find_all('td'))[1].text
    if (ip):
        infos["ip"] = row[0].strong.text

    return infos

def generate_csv(dataFrame):
    """Génère un fichier csv à partir d'une liste des noms de colonnes et des observations associés"""
    return None





if __name__=="__main__":

    driver = webdriver.Chrome(ChromeDriverManager().install())

    print(get_results(driver,"get total number of pages google query google",from_page=1,to_page=-1,website_name=False,url_name=False))


    # Query to obtain links
    # query = 'comprehensive guide to web scraping in python'
    # URL = [] # Initiate empty list to capture final results# Specify number of pages on google search, each page contains 10 #links
    # website_names = []
    # URL_names = []
    # location = []
    #
    # n_pages = 20
    # for page in range(1,3):
    #     url = "http://www.google.com/search?q=" + query + "&start=" + str((page - 1) * 10)
    #
    #     driver.get(url)
    #     soup = BeautifulSoup(driver.page_source, 'html.parser')
    #     # soup = BeautifulSoup(r.text, 'html.parser')
    #
    #     search_URL = soup.find_all('div', class_="yuRUbf")
    #     search_names = soup.find_all('span', class_="VuuXrf")
    #
    #
    #
    #     for h in search_URL:
    #         link = h.a.get('href')
    #         URL.append(link)
    #         URL_names.append(h.h3.text)
    #
    #         url_location = "https://check-host.net/ip-info?host=" + link
    #
    #         driver2.get(url_location)
    #         soup = BeautifulSoup(driver2.page_source, 'html.parser')
    #         # soup = BeautifulSoup(r.text, 'html.parser')
    #
    #         search_location = soup.find('table', class_="hostinfo result")
    #
    #         row = search_location.tbody.find_all('tr')[5]
    #         location.append(row.strong.text)
    #
    #
    #     for name in search_names:
    #         website_names.append(name.text)
    #
    #
    #
    # print(location)
    # print(URL_names)