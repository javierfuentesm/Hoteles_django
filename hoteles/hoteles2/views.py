from django.shortcuts import render
from django.http import JsonResponse
#from habitaciones.forms import RegisterFormModel
from hoteles2.forms import RegisterForm
from hoteles2.models import Hoteles
# Create your views here.

def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        data = form.cleaned_data
        hotel = Hoteles.objects.create(
                nombre=data['nombre'],
                calificacion=data['calificacion']

                )

        return JsonResponse({
                            'El id del hotel es ' :hotel.id,
                            'El nombre del Hotel es' : hotel.nombre,
                            'La calificacion es' : hotel.calificacion

                            })
    return render(request,'hoteles2/hoteles.html',{'form':form})
