from django.db import models
from django.shortcuts import reverse

# Create your models here.

class Client(models.Model):
    SEX = (
        ('M', 'Мужчина'),
        ('F', 'Женщина'),
    )
    LABEL = (
        ('V', 'VIP-клиент'),
        ('K', 'Конфликтный'),
        ('D', 'Должник'),
    )
    first_name = models.CharField(max_length=50, db_index=True)
    last_name = models.CharField(max_length=50, db_index=True)
    sex = models.CharField(max_length=1, choices=SEX)
    phone = models.CharField(max_length=11, db_index=True)
    label = models.CharField(max_length=1, choices=LABEL, blank=True)
    slug = models.SlugField(max_length=150, unique=True)

    def get_absolute_url(self):
        return reverse('client_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.first_name

class Worker(models.Model):
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)

    def __str__(self):
        return self.f_name

class Contractor(models.Model):
    contractor_name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=150, unique=True)

    def get_absolute_url(self):
        return reverse('contractor_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.contractor_name

class Car(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE, related_name='car')
    makes = models.CharField(max_length=80)
    model = models.CharField(max_length=80)
    year = models.CharField(max_length=4, blank=True)
    vin = models.CharField(max_length=25)
    hp = models.FloatField(max_length=5, blank=True)

    def __str__(self):
        return self.makes

class Product(models.Model):
    STATUS = (
        ('A', 'Не закуплен'),
        ('B', 'Ожидается'),
        ('C', 'В наличии'),
        ('D', 'Выдан'),
        ('E', 'Возврат'),
    )
    product_name = models.CharField(max_length=80)
    articul = models.CharField(max_length=20)
    contractor = models.ForeignKey('Contractor', on_delete=models.CASCADE, related_name='product')
    status = models.CharField(max_length=1, choices=STATUS, default='A')
    price_purchase = models.IntegerField(max_length=10)
    price_sale = models.IntegerField(max_length=10)
    info_car = models.CharField(max_length=80)

    def __str__(self):
        return self.product_name

class Order(models.Model):
    STATUS = (
        ('A', 'В работе'),
        ('B', 'Завершен'),
    )
    date_create = models.DateTimeField(auto_now_add=True)
    date_end = models.DateTimeField(blank=True)
    status = models.CharField(max_length=1, choices=STATUS, default='A')
    client = models.ForeignKey('Client', on_delete=models.CASCADE, related_name='order')
    worker = models.ForeignKey('Worker', on_delete=models.CASCADE, related_name='order')
    product = models.ManyToManyField('Product', related_name='order')
    deposit = models.IntegerField(max_length=10, default='0')
    slug = models.SlugField(max_length=150, unique=True)

    def get_absolute_url(self):
        return reverse('order_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.id
