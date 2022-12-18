from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from usuarios.views import UsuarioView
from productos.views import ProductoView
from posts.views import PostView

router = routers.DefaultRouter()
router.register(r"usuarios", UsuarioView, "usuario")
router.register(r"productos", ProductoView, "producto")
router.register(r"posts", PostView, "post")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]
