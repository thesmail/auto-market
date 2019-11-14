from django.shortcuts import render
from django.views.generic import View

from .models import *
from .utils import ObjectDetailMixin

# Create your views here.
def orders_list(request):
    n = ['Oleg', 'Elena', 'Petya']
    return render(request, 'orders/index.html', context={'names':n})

def clients_list(request):
    clients = Client.objects.all()
    return render(request, 'orders/clients_list.html', context={'clients': clients})

class ClientDetail(ObjectDetailMixin, View):
    model = Client
    template = 'orders/client_detail.html'

def cars_list(request):
    cars = Cars.objects.all()
    return render(request, 'orders/cars_list.html', context={'cars': cars})

class CarDetail(ObjectDetailMixin, View):
    model = Cars
    template = 'orders/car_detail.html'
