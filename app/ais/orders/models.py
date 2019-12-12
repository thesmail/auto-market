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
    first_name = models.CharField("Имя", max_length=50, db_index=True)
    last_name = models.CharField("Фамилия", max_length=50, db_index=True)
    fath_name = models.CharField("Отчество", max_length=50, blank=True)
    sex = models.CharField("Пол", max_length=1, choices=SEX, default='M')
    phone = models.CharField("Телефон", max_length=11, db_index=True)
    label = models.CharField("Метка", max_length=1, choices=LABEL, blank=True)

    def get_absolute_url(self):
        return reverse('client_detail_url', kwargs={'pk': self.pk})

    def __str__(self):
        return self.last_name

class Worker(models.Model):
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)

    def __str__(self):
        return self.f_name

class Contractor(models.Model):
    contractor_name = models.CharField('Название поставщика', max_length=50)

    def __str__(self):
        return self.contractor_name

class Car(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    makes = models.CharField(max_length=80)
    model = models.CharField(max_length=80)
    year = models.CharField(max_length=4, blank=True)
    vin = models.CharField(max_length=25)
    hp = models.FloatField(max_length=5, default=0)

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
    contractor = models.ForeignKey('Contractor', null=True, blank=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=1, choices=STATUS, default='A')
    price_purchase = models.FloatField(max_length=20)
    price_sale = models.FloatField(max_length=20)
    info_car = models.CharField(max_length=80)

    def __str__(self):
        return self.product_name

class Order(models.Model):
    STATUS = (
        ('A', 'В работе'),
        ('B', 'Завершен'),
    )
    date_create = models.DateTimeField(auto_now_add=True)
    date_end = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=1, choices=STATUS, default='A')
    client = models.ForeignKey('Client', on_delete=models.CASCADE, verbose_name="Клиент")
    worker = models.ForeignKey('Worker', on_delete=models.CASCADE, verbose_name="")
    product = models.ManyToManyField('Product', related_name='order')
    summa = models.FloatField(max_length=20, default='0')
    deposit = models.FloatField(max_length=20, default='0')
    debt = models.FloatField(max_length=20, default='0')
    note = models.CharField(max_length=150, blank=True)

    def get_absolute_url(self):
        return reverse('order_detail_url', kwargs={'pk': self.pk})

    def __str__(self):
        return '{}'.format(self.id)
