"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include
from django.views.static import serve
from django.conf import settings
from accounts.views import signup, show_profile
from products.views import product_list, product_detail
from cart.views import add_to_cart, remove_from_cart, view_cart
from checkout.views import show_checkout, submit_payment
from django.conf import settings
from django.conf.urls.static import  static
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from  .settings.local import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', product_list, name="home"),
    path('products/<int:id>', product_detail, name="product_detail"),
    path('cart/add/', add_to_cart, name='add_to_cart'),
    path('cart/remove/', remove_from_cart, name='remove_from_cart'),
    path('cart/view/', view_cart, name='view_cart'),
    path('checkout/view/', show_checkout, name='show_checkout'),
    path('checkout/pay/', submit_payment, name='submit_payment'),

    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', signup, name='signup'),
    path('accounts/profile/', show_profile, name='profile'),
    path('media/<path:path>', serve, {'document_root': MEDIA_ROOT}),
 ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

