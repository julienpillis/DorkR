import time
from selenium.webdriver.chrome.service import Service
from features import *
from app import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os





if __name__=="__main__":


    #starting_app()
    end = False
    try :
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
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
        if(function=="dork"):
            query = input(">>>> Insert your dork : ")

            launch_scraping(driver, query, params)

    print(">>>> See yaaa (づ￣ ³￣)づ ")
    time.sleep(3)
    print()







