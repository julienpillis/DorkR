from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

#nombre de page max ?
def get_results(driver,query,dataFrame,url = True, url_name = True,website_name = True, description = False, deep_info = False):
    """Retourne les résultats scrappés d'une requête"""
    return None


def get_location(driver,url,country = True, region = False, ip = False):
    """ Retourne les informations relatives à la géolocalisation d'une URL"""
    return None

def generate_csv(dataFrame):
    """Génère un fichier csv à partir d'une liste des noms de colonnes et des observations associés"""
    return None





if __name__=="__main__":

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver2 = webdriver.Chrome(ChromeDriverManager().install())

    # Query to obtain links
    query = 'comprehensive guide to web scraping in python'
    URL = [] # Initiate empty list to capture final results# Specify number of pages on google search, each page contains 10 #links
    website_names = []
    URL_names = []
    location = []

    n_pages = 20
    for page in range(1,3):
        url = "http://www.google.com/search?q=" + query + "&start=" + str((page - 1) * 10)

        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        # soup = BeautifulSoup(r.text, 'html.parser')

        search_URL = soup.find_all('div', class_="yuRUbf")
        search_names = soup.find_all('span', class_="VuuXrf")



        for h in search_URL:
            link = h.a.get('href')
            URL.append(link)
            URL_names.append(h.h3.text)

            url_location = "https://check-host.net/ip-info?host=" + link

            driver2.get(url_location)
            soup = BeautifulSoup(driver2.page_source, 'html.parser')
            # soup = BeautifulSoup(r.text, 'html.parser')

            search_location = soup.find('table', class_="hostinfo result")

            row = search_location.tbody.find_all('tr')[5]
            location.append(row.strong.text)


        for name in search_names:
            website_names.append(name.text)



    print(location)
    print(URL_names)