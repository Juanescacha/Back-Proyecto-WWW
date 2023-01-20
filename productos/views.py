from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Product
from webscraping.wom_bs4 import wom_ws
from webscraping.xiaomi_store_bs4 import xiaomi_ws
from webscraping.xiaomi_phonelectrics import xiaomi_phonelectrics
from webscraping.iphone import iphone
from webscraping.iphone_cleversel import iphone_cleversel
from webscraping.iphone_merlib import iphone_merlib
from webscraping.samsung_merlib import samsumg_merlib
from webscraping.samsung_cleversel import samsung_cleversel
from webscraping.samsung_phonelectrics import samsung_phonelectrics


# Create your views here.
class ProductApiView(APIView):

    def get(self, request):
        products = Product.objects.all().values()
        return Response(products)

    # realizar el web-scraping
    def post(self, request):
        Product.objects.all().delete()

        #iphone() pendiente arreglar los nombres
        #iphone_cleversel() pendiente mostrar bien los precios
        iphone_merlib()
        xiaomi_phonelectrics() # <- iphone 

        samsumg_merlib()
        #samsung_cleversel() pendiente mostrar bien los precios
        samsung_phonelectrics()

        xiaomi_ws()
        wom_ws() # <- xiaomi

        print('Se ha realizado el webscraping, se guardaron los productos en la base de datos.')
        products = Product.objects.all().values()
        return Response(products)
