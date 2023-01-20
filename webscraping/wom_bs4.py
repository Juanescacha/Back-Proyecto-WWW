from bs4 import BeautifulSoup
import requests
import re
import json
import os

from .save_into_db import get_baseproduct_id
from productos.models import Product


def wom_ws():
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36",
    }

    wom_urls = [
            'https://www.wom.co/equipos?brand=205',
        ]

    address = 'Cra. 24 #52 - 77, Teusaquillo, Bogotá, Cundinamarca'
    lista_productos = []

    for url in wom_urls:
        page = requests.get(url, headers=headers)#, headers=headers)#, params={"q": "python"})
        print('status code:', page.status_code)
        soup = BeautifulSoup(page.content, 'html.parser')
        productos = soup.find_all('li', 
            attrs={'class':'item product product-item'}
            )
        
        for producto in productos:
            a = producto.find('a', attrs={
                'class': 'product-item-link',
            })
            
            name = a.get('title')
            url_p = a.get('href')

            img = producto.find('img', attrs={
                'class': 'product-image-photo',
            })
            img_url = img.get('src')

            span = producto.find('span', attrs={
                'class': 'price',
            })
            price = span.get_text()

            base_product_id = get_baseproduct_id(name)

            p = Product(
                name=name,
                price=price,
                url_image=img_url,
                url_origin=url_p,
                vendor_address=address,
                base_product=None if not base_product_id else base_product_id,
            )
            p.save()


if __name__ == '__main__':
    wom_ws(urls)