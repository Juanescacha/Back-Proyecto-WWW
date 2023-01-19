import requests
from bs4 import BeautifulSoup
from productos.models import Product
from webscraping.save_into_db import get_baseproduct_id

def extraData():
   
    baseUrl = "https://www.phonelectrics.com/collections/apple-celulares"
    response = requests.get(baseUrl)
    soup = BeautifulSoup(response.text, 'html.parser')
    #print(soup)

    for div in soup.find_all("div", class_="grid-view-item"):
        print("===================")
        nombre = (div.find("div", class_="product-grid--title").a.string)
        precio = (div.find("span", class_="money sale-price").text)
        url_celular = (div.find("div", class_="grid-view-item-image").a["href"])
        url_imagen = (div.find("div", class_="grid-view-item-image").img["src"])
        base_product_id = get_baseproduct_id(nombre)
   
        print(nombre)
        print(precio)
        print("https://www.phonelectrics.com"+url_celular)
        print(url_imagen)
        
        p = Product(
                    name= nombre,
                    price= precio,
                    url_image=url_imagen,
                    url_origin=url_celular,
                    vendor_address = '',
                    base_product = None if not base_product_id else base_product_id.id,
                )
        p.save()