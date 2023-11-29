from django import forms
from django.contrib import admin
from .models import *
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.hashers import make_password

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ReservaForm, self).__init__(*args, **kwargs)

        ambiente_nombre = self.initial.get('ambiente')

    
class HiddenPasswordInput(forms.widgets.PasswordInput):
    def render(self, name, value, attrs=None, renderer=None):
        if value:
            value = '*' * len(value)
        return super().render(name, value, attrs, renderer)

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'
        exclude = ['token']
        widgets = {
            'password': HiddenPasswordInput(),
        }

    def clean_password(self):
        password = self.cleaned_data['password']
        if password:
            return make_password(password)
        return password