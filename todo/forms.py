from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UReg(UserCreationForm):
    """
    Форма регистрации
    """
    username = forms.CharField(label='Логин')
    first_name = forms.CharField(label='Имя')
    last_name = forms.CharField(label='Фамилия')
    email = forms.EmailField(label='Почта')
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторный пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


def clean_password(self):
    cd = self.cleaned_data
    if cd['password'] != cd['password']:
        raise forms.ValidationError('Пароли не совпадают')
    return cd['password']