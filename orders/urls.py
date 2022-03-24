from unicodedata import name
from django import views
from django.urls import path
from . import views
urlpatterns = [
    path('add_to_cart', views.add_to_cart , name='add_to_cart'),
    path('',views.cart , name='cart'),
    path('remove_cart/<int:id>', views.remove_cart , name='remove_cart'),
]
