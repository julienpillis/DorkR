import time
from selenium.webdriver.chrome.service import Service
from features import *
from app import *
import os




if __name__=="__main__":
    starting_app()


    end = False
    while(not end):
        entry = input(">>>>?")
        if(entry.lower()=="exit"): end = True
        if(entry.lower()=="dork"):
            query = input(">>>> Insert your dork : ")
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            print(launch_query(driver, query))

    print(">>>> See yaaa pilot (づ￣ ³￣)づ ")
    time.sleep(3)







