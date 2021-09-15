#!/usr/bin/env python
# coding: utf-8

# In[63]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import numpy as np
import pandas as pd
import re
from datetime import datetime, timedelta
import requests
from time import sleep
import os
from zipfile import ZipFile 
from selenium.webdriver.support.ui import Select


# In[113]:


driver = webdriver.Chrome(executable_path=r"C:/Users/andrea farchetto/Downloads/chromedriver_win32/chromedriver.exe")

url = "https://www.padron.gob.ar/publica/"

driver.get(url)

element = driver.find_element_by_xpath('//*[@id="site"]')

sleep(3)
drp = Select(element)

sleep(2)

drp.select_by_visible_text('CORDOBA')

sleep(3)
zona = driver.find_element_by_xpath('//*[@id="tabred"]')
zona.click()

seccion = driver.find_element_by_xpath('//*[@id="secc"]')

sleep(3)
secc = Select(seccion)


# In[114]:


g = [i.strip() for i in seccion.text.split('\n')]
districto = [t for t in g if len(t)>0]


# In[ ]:


for elemento in districto:
    
    element = driver.find_element_by_xpath('//*[@id="secc"]')
    drp = Select(element)
    drp.select_by_visible_text(elemento)
    
    s = driver.find_element_by_xpath('//*[@id="circ"]')
    c = [i.strip() for i in s.text.split('\n')]
    circuito = [t for t in c if len(t)>0]
    
    for circ in circuito:
        while True:
            try:
                element = driver.find_element_by_xpath('//*[@id="circ"]')
                drp = Select(element)
                drp.select_by_visible_text(circ)
                break
            except:
                pass
        
        driver.find_element_by_xpath('//*[@id="btnVer"]').click()
        
        while True:
            try:
                driver.find_element_by_xpath('//*[@id="btnExcel"]').click()
                break
            except:
                pass
        
        driver.find_element_by_xpath('//*[@id="btnVolver"]').click()


# In[ ]:




