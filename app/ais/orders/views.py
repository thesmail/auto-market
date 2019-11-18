from django.shortcuts import render
from django.views.generic import View

from .models import *
from .utils import ObjectDetailMixin

# Create your views here.
def orders_list(request):
    orders = Order.objects.all()
    return render(request, 'orders/index.html', context={'orders': orders})

class OrderDetail(ObjectDetailMixin, View):
    model = Order
    template = 'orders/order_detail.html'

def clients_list(request):
    clients = Client.objects.all()
    return render(request, 'orders/clients_list.html', context={'clients': clients})

class ClientDetail(ObjectDetailMixin, View):
    model = Client
    template = 'orders/client_detail.html'
