# forms.py
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.forms import ModelForm, ModelChoiceField, ModelMultipleChoiceField, CheckboxSelectMultiple
from .models import *
from .forms import *
from django.db import transaction

class PizzaForm(forms.ModelForm):

    toppings = forms.ModelMultipleChoiceField(
        queryset=Toppings.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    class Meta:
        model = Pizza
        fields = ['size', 'crust', 'sauce', 'cheese', 'toppings']

class PaymentForm(forms.ModelForm):
    class Meta:
        model = PaymentInfo
        fields = ['name_on_card', 'card_number', 'expiration_month', 'expiration_year', 'cvv', 'address_line_1', 'address_line_2', 'city', 'state', 'country', 'zip_code']
        labels = {
            'name_on_card': 'Full Name',
            'card_number': 'Card Number',
            'expiration_month': 'Expiry Month',
            'expiration_year': 'Expiry Year',
            'cvv': 'CVV',
            'address_line_1': 'Address Line 1',
            'address_line_2': 'Address Line 2',
            'zip_code': 'Zip Code'

        }
        widgets = {
            'card_number': forms.TextInput(attrs={'pattern': '[0-9]{16}', 'title': '16 digits required'}),
            'expiration_month': forms.TextInput(attrs={'pattern': '[0-9]{2}', 'title': '2 digits required'}),
            'expiration_year': forms.TextInput(attrs={'pattern': '[0-9]{4}', 'title': '4 digits required'}),
            'cvv': forms.TextInput(attrs={'pattern': '[0-9]{3}', 'title': '3 digits required'})
        }

class UserSignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_admin = False
        user.email = self.cleaned_data['username']
        user.save()
        return user
    
class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)