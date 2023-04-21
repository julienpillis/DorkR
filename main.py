import time
from selenium.webdriver.chrome.service import Service
from features import *
from app import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os




if __name__=="__main__":


    starting_app()
    end = False
    try :
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    except :
        end = True
        print("Webdriver installation failed. Please make sur you have Chrome.")
    while(not end):
        entry = input(">>>>? ")
        if(entry.lower()=="exit"): end = True
        if(entry.lower()=="dork"):
            query = input(">>>> Insert your dork : ")

            launch_query(driver, query)

    print(">>>> See yaaa (づ￣ ³￣)づ ")
    time.sleep(3)
    print()







