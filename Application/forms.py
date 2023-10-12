from django import forms
from .models import Customer, CustomerContact
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta():
        model = Customer
        fields = ('email', 'username', 'password1', 'password2')


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

