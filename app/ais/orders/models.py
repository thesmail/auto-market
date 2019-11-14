from django.db import models
from django.shortcuts import reverse

# Create your models here.

class Status(models.Model):
    status = models.CharField(max_length=150, db_index=True)

    def __str__(self):
        return '{}'.format(self.name)

class Client(models.Model):
    first_name = models.CharField(max_length=50, db_index=True)
    last_name = models.CharField(max_length=50, db_index=True)
    phone = models.CharField(max_length=11, db_index=True)
    note_c = models.CharField(max_length=150, blank=True)
    slug = models.SlugField(max_length=150, unique=True)

    def get_absolute_url(self):
        return reverse('client_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.first_name

class Car(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE, related_name='cars')
    manufacturer = models.CharField(max_length=150)
    model = models.CharField(max_length=150)
    year = models.CharField(max_length=4)
    vin_body = models.CharField(max_length=40, blank=True)
    horsepower = models.FloatField(max_length=5)
    slug = models.SlugField(max_length=150, unique=True)

    def get_absolute_url(self):
        return reverse('car_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.manufacturer

class Order(models.Model):
    date_create = models.DateTimeField(auto_now_add=True)
    date_end = models.DateTimeField(blank=True)
    client = models.ForeignKey('Client', on_delete=models.CASCADE, related_name='orders')
    car = models.ForeignKey('Car', on_delete=models.CASCADE, related_name='order')
    product = models.ManyToManyField('Product', related_name='order')
    deposit = model.IntegerField(max_length=10)
    note_o = models.CharField(max_length=150, blank=True)
    slug = models.SlugField(max_length=150, unique=True)

    def get_absolute_url(self):
        return reverse('order_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.id

class Product(models.Model):
    name_p = models.CharField(max_length=150)
    articul = models.CharField(max_length=40)
    contractor = models.ForeignKey('Contractor', on_delete=models.CASCADE, related_name='products')
    price = model.IntegerField(max_length=10)
    quantity = model.IntegerField(max_length=5)
    status = models.ForeignKey('Status', on_delete=models.CASCADE, related_name='products')

class Contractor(models.Model):
    name_c = models.CharField(max_length=40)
    slug = models.SlugField(max_length=150, unique=True)
