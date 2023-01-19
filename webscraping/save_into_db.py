import json
import re

from .regex import base_products
from productos.models import Product, BaseProduct

def get_baseproduct_id(product_name):
    for bp_name in base_products:
        for regexp in base_products[bp_name]:
            if re.match(regexp, product_name.lower()):
                return BaseProduct.objects.get(name=bp_name)
    return None


def save_products(path_to_products):
    with open(path_to_products, 'r') as file:
        products = json.load(file)
        for product in products:
            name = product['name']
            base_product_id = get_baseproduct_id(name)
            if base_product_id == None:
                print(f"No se ha encontrado el producto_base para {name}, no se pudo agregar el producto.")
            else:
                p = Product(
                    name=name,
                    price=product['price'],
                    url_image=product['url_image'],
                    url_origin=product['url_origin'],
                    vendor_address=product['vendor_address'],
                    base_product=base_product_id,
                )
                p.save()