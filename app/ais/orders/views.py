from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import View
from django.views import generic

from .models import *
from .forms import *
from .utils import ObjectDetailMixin
from bootstrap_modal_forms.generic import (BSModalCreateView,
                                           BSModalUpdateView,
                                           BSModalReadView,
                                           BSModalDeleteView)

# Create your views here.
class ContractorCreateView(BSModalCreateView):
    template_name = 'crud/create_contractor.html'
    form_class = ContractorForm
    success_message = 'Отлично! Поставщик создан'
    success_url = reverse_lazy('contractors_list_url')

class ContractorDeleteView(BSModalDeleteView):
    model = Contractor
    template_name = 'crud/delete_contractor.html'
    success_message = 'Успешно удален поставщик'
    success_url = reverse_lazy('contractors_list_url')

class ClientCreateView(BSModalCreateView):
    template_name = 'crud/create_client.html'
    form_class = ClientForm
    success_message = 'Отлично! Клиент создан'
    success_url = reverse_lazy('clients_list_url')

class ClientUpdateView(BSModalUpdateView):
    model = Client
    template_name = 'crud/update_client.html'
    form_class = ClientForm
    success_message = 'Информация о клиенте обновлена'
    success_url = reverse_lazy('clients_list_url')

class ClientDeleteView(BSModalDeleteView):
    model = Client
    template_name = 'crud/delete_client.html'
    success_message = 'Клиент успешно удален'
    success_url = reverse_lazy('clients_list_url')

class CarCreateView(BSModalCreateView):
    template_name = 'crud/create_car.html'
    form_class = CarForm
    success_message = 'Отлично! Машина добавлена'
    success_url = reverse_lazy('client_detail_url')

class CarUpdateView(BSModalUpdateView):
    model = Client
    template_name = 'crud/update_client.html'
    form_class = ClientForm
    success_message = 'Информация о клиенте обновлена'
    success_url = reverse_lazy('clients_list_url')

class CarDeleteView(BSModalDeleteView):
    model = Client
    template_name = 'crud/delete_client.html'
    success_message = 'Клиент успешно удален'
    success_url = reverse_lazy('clients_list_url')

def orders_list(request):
    orders = Order.objects.all()
    return render(request, 'orders/orders_list.html', context={'orders': orders})

class OrderDetail(ObjectDetailMixin, View):
    model = Order
    template = 'orders/order_detail.html'

def clients_list(request):
    clients = Client.objects.all()
    return render(request, 'orders/clients_list.html', context={'clients': clients})

class ClientDetail(ObjectDetailMixin, View):
    model = Client
    template = 'orders/client_detail.html'

def contractors_list(request):
    contractors = Contractor.objects.all()
    return render(request, 'orders/contractors_list.html', context={'contractors': contractors})
