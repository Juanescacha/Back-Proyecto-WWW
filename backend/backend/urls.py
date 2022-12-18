from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from usuarios import views

router = routers.DefaultRouter()
router.register(r"usuarios", views.UsuarioView, "usuario")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]
