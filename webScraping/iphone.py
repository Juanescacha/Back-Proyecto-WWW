from selenium import webdriver
import os 
import driver
import requests
from bs4 import BeautifulSoup 

def extraData():
    
    baseUrl = "https://tiendasishop.com/co/iphone"

    response = requests.get(baseUrl)

    soup = BeautifulSoup(response.text, 'html.parser')
    #print(soup) 

    lista_link = []
    for div in soup.find_all("li", class_="item product product-item"):
     #print("===================")
     #print(div.find("div",class_="vtex-product-summary-2-x-nameContainer flex items-start justify-center pv6").h3.string)
     #print(div.find("div",class_="co16-discover-column-new__description-wrapper").p.string)
     #print(div.find("div", class_="product-item-info").a["href"])
     # print(div.find("div",class_="image image--main-loaded").img.get('src')) 
     
     url_celular = div.find("div", class_="product-item-info").a["href"]
     lista_link.append(url_celular)
    # print(url_celular)
     
    for url in lista_link:
        driver.get(url)
        driver.get("https://tiendasishop.com/co/iphone-12-64gb-blanco-mgj63lz-a")  
     
extraData()