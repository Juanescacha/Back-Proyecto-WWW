import requests
from bs4 import BeautifulSoup
#from productos.models import Product
#import save_into_db

def extraData():
    
    baseUrl = "https://listado.mercadolibre.com.co/xiaomi#D[A:xiaomi]"
    response = requests.get(baseUrl)
    soup = BeautifulSoup(response.text, 'html.parser')
    #print(soup) 

    for div in soup.find_all("li", class_="ui-search-layout__item shops__layout-item"):
      print("===================")
      print(div.find("div",class_="ui-search-item__group ui-search-item__group--title shops__items-group").h2.string)
      print(div.find("span",class_="price-tag-amount").text)
      print(div.find("div",class_="ui-search-result__image shops__picturesStyles").a["href"])
      print(div.find("div",class_="slick-slide slick-active").img["data-src"])

extraData()