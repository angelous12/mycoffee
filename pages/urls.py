from django import views
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index , name='index'),
    path('product/<str:slug>', views.product , name='product'),
]
