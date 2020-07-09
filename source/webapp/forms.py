from django import forms
from django.forms import widgets
from webapp.models import PRODUCT_CATEGORY_CHOICE


class ProductForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label='Name')
    description = forms.CharField(max_length=2000, required=True, label='Description',
                                  widget=widgets.Textarea)
    category = forms.ChoiceField(choices=PRODUCT_CATEGORY_CHOICE, required=False, label='Category')
    amount = forms.IntegerField(min_value=0, label='amount')
    price = forms.DecimalField(max_digits=7, decimal_places=2, label='price')