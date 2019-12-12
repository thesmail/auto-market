from django.urls import path

from .views import *

urlpatterns = [
    path('', orders_list, name='orders_list_url'),
    path('clients/', clients_list, name='clients_list_url'),
    path('client/create', ClientCreateView.as_view(), name='create_client'),
    path('client/update/<int:pk>', ClientUpdateView.as_view(), name='update_client'),
    path('client/delete/<int:pk>', ClientDeleteView.as_view(), name='delete_client'),
    path('client/<int:pk>', ClientDetail.as_view(), name='client_detail_url'),

    path('car/create', CarCreateView.as_view(), name='create_car'),
    path('car/update/<int:pk>', CarUpdateView.as_view(), name='update_car'),
    path('car/delete/<int:pk>', CarDeleteView.as_view(), name='delete_car'),

    path('order/<int:pk>', OrderDetail.as_view(), name='order_detail_url'),

    path('contractors/', contractors_list, name='contractors_list_url'),
    path('contractor/create', ContractorCreateView.as_view(), name='сreate_contractor'),
    path('contractor/delete/<int:pk>', ContractorDeleteView.as_view(), name='delete_contractor'),

]
