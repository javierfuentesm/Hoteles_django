from django.forms import ModelForm
from django import forms
from habitaciones.models import Habitaciones




class RegisterFormModel(forms.ModelForm):

    class Meta:
        model= Habitaciones
        fields=['piso','numero','costo_x_dia','capacidad','id_hotel_id']
