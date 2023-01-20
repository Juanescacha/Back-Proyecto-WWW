from bs4 import BeautifulSoup
import requests
import re
import json
import os

from .save_into_db import get_baseproduct_id
from productos.models import Product


def xiaomi_ws():
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

            p = Product(
                name=name,
                price=producto.get('data-price'),
                url_image=producto.get('data-image-url'),
                url_origin=producto.get('data-url'),
                vendor_address=address,
                base_product=None if not base_product_id else base_product_id,
            )
            p.save()
        


if __name__ == '__main__':
    xiaomi_ws(xiaomi_urls)