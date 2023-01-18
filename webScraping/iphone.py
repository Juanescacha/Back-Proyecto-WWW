from selenium import webdriver
import os 
import driver
import requests
from bs4 import BeautifulSoup
import  conexion_bd

def extraData(tableName):
    
    conexion_bd.truncateTable(tableName)
    
    baseUrl = "https://tiendasishop.com/co/iphone"
    response = requests.get(baseUrl)
    soup = BeautifulSoup(response.text, 'html.parser')
    #print(soup) 

    for div in soup.find_all("li", class_="item product product-item"):
     print("===================")
     railway = []
     nombre = (div.find("div",class_="product details product-item-details").a.string)
     precio = (div.find("span",class_="price-container price-final_price tax weee").span.string)
     url_celular = (div.find("div", class_="product-item-info").a["href"])
     url_imagen = (div.find("span",class_="product-image-wrapper").img["data-src"]) 
       
     railway.append(nombre)
     railway.append(precio)
     railway.append(url_celular)
     railway.append(url_imagen)
     
     print(railway[0])
     
    conexion_bd.inserData(railway, tableName)
     
extraData('public.scraping_celular')