import requests
from bs4 import BeautifulSoup
from productos.models import Product
from webscraping import save_into_db

def samsung_phonelectrics():
   
    baseUrl = "https://www.phonelectrics.com/collections/celulares-samsung-galaxy"
    response = requests.get(baseUrl)
    soup = BeautifulSoup(response.text, 'html.parser')
    #print(soup)

    for div in soup.find_all("div", class_="grid-view-item"):
        print("===================")
        nombre = (div.find("div", class_="product-grid--title").a.string)
        precio =(div.find("span", class_="money sale-price").text)
        url_celular = "https://www.phonelectrics.com"+(div.find("div", class_="grid-view-item-image").a["href"])
        url_imagen = "https:"+(div.find("div", class_="grid-view-item-image").img["src"])
        base_product_id = save_into_db.get_baseproduct_id(nombre)
        
        print(nombre)
        print(precio)
        print(url_celular)
        print(url_imagen)
        
        p = Product(
            name= nombre,
            price= precio,
            url_image=url_imagen,
            url_origin=url_celular,
            vendor_address = 'Av El Dorado # 68C - 61 Torre Central Davivienda Bogotá - Colombia',
            base_product = None if not base_product_id else base_product_id,
        )
        p.save()