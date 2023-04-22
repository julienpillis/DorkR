import time
from selenium.webdriver.chrome.service import Service
from features import *
from app import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os

def input_listener():
    """Listen and prepare the user entry for processing"""
    entry = input(">>>>? ")
    entry = entry.split(sep='(')
    function = entry[0]
    params = []
    if function not in ['exit', 'dork', 'import']:
        print("      Bad entry. Please check your query.")
    else :
        if (len(entry) >= 2):
            if function == "dork" :

                params_tmp = entry[1].split(')')[0].split(sep=',')
                params = [param for param in params_tmp if param in ["country","region","city","ip","url_name","short_url","url"]]
    print(function)
    print(params)
    return function,params



if __name__=="__main__":


    #starting_app()
    end = False
    try :
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        print("Webdriver is set. Ready to go !")
    except :
        end = True
        print("Webdriver installation failed. Please make sur you have Chrome.")

    while(not end):
        entry = input_listener()
        function = entry[0]
        params = entry[1]
        if(function=="exit"): end = True
        if(function=="dork"):
            query = input(">>>> Insert your dork : ")

            launch_query(driver, query)

    print(">>>> See yaaa (づ￣ ³￣)づ ")
    time.sleep(3)
    print()







