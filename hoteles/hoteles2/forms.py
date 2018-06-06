from django.forms import ModelForm
from django import forms
from hoteles2.models import Hoteles


# Create the form class.
class RegisterFormModel(forms.ModelForm):
    class Meta:
        model= Hoteles
        fields=['nombre','calificacion']

    
