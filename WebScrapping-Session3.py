# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
df = pd.read_csv("C:/Users/Workstate/Downloads/output2.csv", sep=',')

for index, row in df[pd.isnull(df['formula'])].iterrows():
    if index < 300:
        print(index)
        
for index, row in df[pd.isnull(df['formula'])].iterrows():
        chemform = obtainChemformula(row['url'])
        df.at[index, 'formula'] = chemform
        time.sleep(3)

 df[~pd.isnull(df['formula'])].to_csv("out_final.csv")    

def obtainChemformula(url):
    chem_found = ''    
    driver = webdriver.Firefox()
    driver.get(url)
    delay = 20 # seconds
    try:
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID,"nav-tech")))
        print("Page is ready!")
        element= driver.find_element(By.ID,"nav-tech")
        elems = element.find_elements(By.CLASS_NAME,"row");
        for idx,e in enumerate(elems):
            #print('--',e.text,'--')
            if "Chemical Formula" in e.text:
                #found chemical formula
                chem_found = e.text.replace("Chemical Formula", "").strip()
        #element.clear()
        driver.close()
    except TimeoutException:
        print("Loading took too much time!")
        driver.close()
    return chem_found