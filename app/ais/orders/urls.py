from django.urls import path

from .views import *

urlpatterns = [
    path('', orders_list, name='orders_list_url'),
    path('clients/', clients_list, name='clients_list_url'),
    path('client/<str:slug>', ClientDetail.as_view(), name='client_detail_url'),
    path('order/<str:slug>', OrderDetail.as_view(), name='order_detail_url'),


]
