from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class registrationForm(UserCreationForm):

    class Meta:

        model = User
        fields = ['email', 'username', 'password1', 'password2']


class purchaseForm(forms.Form):

    offer = forms.IntegerField(max_value=10)
    address = forms.CharField(max_length=100)

