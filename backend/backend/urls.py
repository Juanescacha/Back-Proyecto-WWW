from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from usuarios.views import UsuarioView
from productos.views import ProductoView

router = routers.DefaultRouter()
router.register(r"usuarios", UsuarioView, "usuario")
router.register(r"productos", ProductoView, "producto")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]
