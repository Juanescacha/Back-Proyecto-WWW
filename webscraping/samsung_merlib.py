import requests
from bs4 import BeautifulSoup
from productos.models import Product
from webscraping import save_into_db

def samsumg_merlib():
    
    baseUrl = "https://listado.mercadolibre.com.co/samsung#D[A:samsung]"
    response = requests.get(baseUrl)
    soup = BeautifulSoup(response.text, 'html.parser')
    #print(soup) 

    for div in soup.find_all("li", class_="ui-search-layout__item shops__layout-item"):
        print("===================")
        nombre = (div.find("div",class_="ui-search-item__group ui-search-item__group--title shops__items-group").h2.string)
        precio = (div.find("span",class_="price-tag-amount").text)
        url_celular = (div.find("div",class_="ui-search-result__image shops__picturesStyles").a["href"])
        url_imagen = (div.find("div",class_="slick-slide slick-active").img["data-src"])
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
            vendor_address = 'Carrera 17 Numero 93 - 09 Bogotá D.C., Colombia',
            base_product = None if not base_product_id else base_product_id,
        )
        p.save()