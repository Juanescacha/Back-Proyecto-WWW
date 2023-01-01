from rest_framework import routers
from .api import BaseProductViewSet

router = routers.DefaultRouter()

router.register('api/baseproducts', BaseProductViewSet, 'baseproducts')

urlpatterns = router.urls