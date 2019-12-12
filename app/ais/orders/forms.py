from django import forms

from bootstrap_modal_forms.forms import BSModalForm

from .models import *

class ContractorForm(BSModalForm):
    class Meta:
        model = Contractor
        fields = ['contractor_name']

class ClientForm(BSModalForm, forms.Form):
    phone = forms.CharField(label="Телефон", widget= forms.TextInput(attrs={'id':'phone'}))
    class Meta:
        model = Client
        exclude = ['']

class CarForm(BSModalForm):
    class Meta:
        model = Car
        exclude = ['']
