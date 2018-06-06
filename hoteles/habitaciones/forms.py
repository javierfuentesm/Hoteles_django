from django.forms import ModelForm
from django import forms

# Create the form class.
class RegisterForm(forms.Form):
     piso=forms.CharField(label='piso')
     numero=forms.CharField(label='Numero')
     costo=forms.CharField(label='Costo')
     capacidad=forms.CharField(label='Capacidad')
     idhotel=forms.CharField(label='Id Hotel')
