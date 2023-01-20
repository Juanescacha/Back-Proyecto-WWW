import requests
from bs4 import BeautifulSoup
from productos.models import Product
from webscraping import save_into_db

def iphone():
    
    baseUrl = "https://tiendasishop.com/co/iphone"
    response = requests.get(baseUrl)
    soup = BeautifulSoup(response.text, 'html.parser')
    #print(soup) 

    for div in soup.find_all("li", class_="item product product-item"):
        print("===================")
        nombre = div.find("a",class_="product-item-link").get_text()
        precio = (div.find("span",class_="price-container price-final_price tax weee").span.string)
        url_celular = (div.find("div", class_="product-item-info").a["href"])
        url_imagen = (div.find("span",class_="product-image-wrapper").img["data-src"])
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