from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Product
from webscraping.wom_bs4 import wom_ws
from webscraping.xiaomi_store_bs4 import xiaomi_ws
from webscraping.xiaomi_phonelectrics import xiaomi_phonelectrics
from webscraping.save_into_db import save_products

# Create your views here.
class ProductApiView(APIView):

    def get(self, request):
        products = Product.objects.all().values()
        return Response(products)

    # realizar el web-scraping
    def post(self, request):
        Product.objects.all().delete()

        xiaomi_phonelectrics()
        xiaomi_ws()
        wom_ws()

        print('Se ha realizado el webscraping, se guardaron los productos en la base de datos.')
        products = Product.objects.all().values()
        return Response(products)
