from bs4 import BeautifulSoup
import requests
import re
import json
import os

from .save_into_db import get_baseproduct_id


def xiaomi_ws(file_name):
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36",
    }

    xiaomi_urls = [
        'https://www.xiaomi-store.co/smartphones',
        'https://www.xiaomi-store.co/smartphones?page=2',
    ]

    address = 'Calle 59 # 5 - 30 Bogotá, D.C'

    lista_productos = []

    for url in xiaomi_urls:
        page = requests.get(url, headers=headers)#, headers=headers)#, params={"q": "python"})
        print('status code:', page.status_code)
        soup = BeautifulSoup(page.content, 'html.parser')
        productos = soup.find_all('div', 
            attrs={'class':'vtex-yotpo-1-x-ratingInlineContainer'}
            )

        for producto in productos:
            name = producto.get('data-name')
            base_product_id = get_baseproduct_id(name)

            lista_productos.append(
                {
                    'name': name,
                    'url_origin': producto.get('data-url'),
                    'url_image': producto.get('data-image-url'),
                    'vendor_address': address,
                    'is_active': True,
                    'price': producto.get('data-price'), 
                    'base_product': base_product_id.id,
                },
            )
    with open(file_name, 'w') as f:
        json.dump(
            lista_productos, 
            f,
        ) 


if __name__ == '__main__':
    xiaomi_ws(xiaomi_urls)