"""Ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path
from ecommerce_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r"^login/(?P<id>[0-9]+)?$", Login.as_view(),name="login"),
    re_path(r"^home/(?P<id>[0-9]+)?$", Home.as_view(),name="home"),
    re_path(r"^cart/(?P<id>[0-9]+)?$", Cart.as_view(),name="cart"),
    re_path(r"^search/(?P<id>[0-9]+)?$", Search.as_view(),name="search"),
    path("logout",logoutView,name="logout"),
    re_path(r"^checkout/(?P<id>[0-9]+)?$", Checkout.as_view(),name="checkout"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
