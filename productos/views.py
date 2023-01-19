from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Product
from webscraping.wom_bs4 import wom_ws
from webscraping.xiaomi_store_bs4 import xiaomi_ws
from webscraping.save_into_db import save_products
from webscraping.xiami_phonelectrics import extraData

# Create your views here.
class ProductApiView(APIView):

    def get(self, request):
        products = Product.objects.all().values()
        return Response(products)

    # realizar el web-scraping
    def post(self, request):
        names = [
            'products.json',
            'products_wom.json'
        ]
         #xiaomi_ws('webscraping/products.json')
         #wom_ws('webscraping/products_wom.json')
         
        extraData()

        #for name in names:
           # save_products('webscraping/'+name)
           
        print('Se ha realizado el webscraping, se guardaron los productos en la base de datos.')
        products = Product.objects.all().values()
        return Response(products)
