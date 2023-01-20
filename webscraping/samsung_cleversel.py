import requests
from bs4 import BeautifulSoup
from productos.models import Product
from webscraping import save_into_db
import re

def samsung_cleversel():
   
    baseUrl = "https://www.clevercel.co/collections/samsung"
    response = requests.get(baseUrl)
    soup = BeautifulSoup(response.text, 'html.parser')
    #print(soup)

    for div in soup.find_all("product-item", class_="product-item"):
        print("===================")
        nombre = (div.find("div", class_="product-item-meta").a.string)
        precio = (div.find("span", class_="price").text)
        patron = '[a-z, A-Z]'
        result_precio = re.sub(patron, '', precio)
        
        url_celular = "https://www.clevercel.co"+(div.find("div",class_="product-item__image-wrapper").a["href"])
        url_imagen = "https:"+(div.find("div",class_="product-item__image-wrapper").img["src"])
        base_product_id = save_into_db.get_baseproduct_id(nombre)
        
        print(nombre)
        print(precio)
        print(url_celular)
        print(url_imagen)
        
        p = Product(
            name= nombre,
            price= result_precio,
            url_image=url_imagen,
            url_origin=url_celular,
            vendor_address = 'Cra. 51 #183-17 local #2-45, Suba, Bogotá',
            base_product = None if not base_product_id else base_product_id,
        )
        p.save()