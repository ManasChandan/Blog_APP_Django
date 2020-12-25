from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . models import Profiel
from django import forms

class Register(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'first_name' , 'last_name' , 'email' , 'password1' , 'password2']

class UserInfoUpdate(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username' , 'email']

class ProfileUpdate(forms.ModelForm):
    class Meta:
        model = Profiel
        fields = ['image']