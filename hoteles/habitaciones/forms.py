from django.forms import ModelForm
from django import forms
from hoteles2.models import Hoteles

# Create the form class.
class RegisterForm(forms.Form):
     #hoteles={'elements' :Hoteles.objects.values_list('id',flat=True)}
     #print (Hoteles.objects.values_list('id',flat=True))


     piso=forms.CharField(label='piso')
     numero=forms.CharField(label='Numero')
     costo=forms.CharField(label='Costo')
     capacidad=forms.CharField(label='Capacidad')
     idhotel=forms.CharField(label='Id hotel')
