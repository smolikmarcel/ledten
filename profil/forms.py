from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserExtend

class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserExtendRegisterForm(forms.ModelForm):
    phone = forms.CharField(max_length=100)

    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    street = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    PSC = forms.CharField(max_length=100)

    class Meta:
        model = UserExtend
        fields = ['username', 'phone', 'first_name', 'last_name', 'street', 'city', 'PSC']



class UserUpdateForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email']

class UserExtendUpdateForm(forms.ModelForm):
    phone = forms.CharField(max_length=100)

    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    street = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    PSC = forms.CharField(max_length=100)

    class Meta:
        model = UserExtend
        fields = ['username', 'phone', 'first_name', 'last_name', 'street', 'city', 'PSC', 'img']
