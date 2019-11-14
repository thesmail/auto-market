from django.urls import path

from .views import *

urlpatterns = [
    path('', orders_list),
    path('clients/', clients_list, name='clients_list_url'),
    path('client/<str:slug>', ClientDetail.as_view(), name='client_detail_url'),
    path('cars/', cars_list, name='cars_list_url'),
    path('car/<str:slug>', CarDetail.as_view(), name='car_detail_url'),


]
