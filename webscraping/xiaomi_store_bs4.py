from bs4 import BeautifulSoup
import requests
import re
import json
import os

headers = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36",
}

base_products = {
    re.compile('xiaomi\s*11.*'): 0,
    re.compile('poco\s*m5.*'): 1,
    re.compile('xiaomi\s*12.*'): 2,
    re.compile('poco\s*f4.*'): 3,
    re.compile('redmi\s*note\s*11.*'): 4,
    re.compile('redmi\s*10.*'): 5,
    re.compile('poco\s*m4.*'): 6,
    re.compile('poco\s*x4.*'): 7,
    re.compile('redmi\s*a1.*'): 8,
    re.compile('redmi\s*9.*'): 10,
}

xiaomi_urls = [
        'https://www.xiaomi-store.co/smartphones',
        'https://www.xiaomi-store.co/smartphones?page=2',
    ]

def xiaomi_ws(urls):
    lista_productos = []

    for url in urls:
        page = requests.get(url, headers=headers)#, headers=headers)#, params={"q": "python"})
        print('status code:', page.status_code)
        soup = BeautifulSoup(page.content, 'html.parser')
        productos = soup.find_all('div', 
            attrs={'class':'vtex-yotpo-1-x-ratingInlineContainer'}
            )#,  attrs={"class": 'vtex-yotpo-1-x-ratingInlineContainer center yotpo bottomLine yotpo-small'})
        #print(productos)

        for producto in productos:
            name = producto.get('data-name')
            base_product_id = None
            for b_product in base_products:
                if re.match(b_product, name.lower()):
                    base_product_id = base_products[b_product]
                    if base_product_id == 9:
                        print("nombre:", name)
                    break

            lista_productos.append(
                {
                    'name': name,
                    'url_origin': producto.get('data-url'),
                    'url_image': producto.get('data-image-url'),
                    'vendor_address': 'Calle 59 # 5 - 30 Bogotá, D.C',
                    'is_active': True,
                    'price': producto.get('data-price'), 
                    'base_product': base_product_id,
                },
            )
    with open('products_info.json', 'w') as f:
        json.dump(
            lista_productos, 
            f,
        ) 


if __name__ == '__main__':
    xiaomi_ws(xiaomi_urls)