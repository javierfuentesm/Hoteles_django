from django.forms import ModelForm
from django import forms

# Create the form class.
class RegisterForm(forms.Form):
     nombre=forms.CharField(label='Nombre del hotel')
     calificacion=forms.IntegerField(label='Calificacion')
