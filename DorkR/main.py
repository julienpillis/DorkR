import pandas as pd
from selenium.webdriver.chrome.service import Service
from features import launch_scraping, generate_csv
from pandas import read_csv
from time import sleep
from app import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


if __name__=="__main__":
    starting_app()
    end = False
    try :
        options = Options()
        #options.add_argument("--headless")

        #options.binary_location = "YOUR CHROME APP PATH"
        #driver = webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))


        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
        print("     Webdriver is set. Ready to go !")
    except :
        end = True
        driver = None
        print("     Webdriver installation failed. Please make sure you have Chrome.")

    while(not end):
        entry = input_listener()
        function = entry[0]
        params = entry[1]
        if(function=="exit"): end = True
        elif(function=="dork"):
            print_settings(params)
            query = input(">>>> Insert your dork : ")
            print(f"     Scraping query : {query}")
            launch_scraping(driver, query, params)

        elif(function=="dork_csv"):
            try:
               data = pd.DataFrame()
               pages = ask_pages()
               queries = read_csv(f"{params[0]}",header=None)
               print_settings(params[1:])
               for query in queries.iloc[:,0] :
                   print(f"      \nScraping query : {query}")
                   try :
                        res = launch_scraping(driver, query, params[1:],pages[0],pages[1],gen_csv=False)
                        if(data.empty):data = res
                        else : data = pd.concat([data,res])
                   except : print(f"     \nImpossible to scrap : {query}")
               generate_csv(data,"recap queries")

            except Exception as e:
                print(e)
                generate_csv(data,"recap queries")
                print("     Unable to open and/or read the file... Please check the path and/or the file format.")


    driver.quit()
    print(">>>> Bye bye (づ￣ ³￣)づ ")
    sleep(3)
    print()







