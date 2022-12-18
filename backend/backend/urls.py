from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from usuarios.views import UsuarioView

router = routers.DefaultRouter()
router.register(r"usuarios", UsuarioView, "usuario")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]
