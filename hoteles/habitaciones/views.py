from django.shortcuts import render
from django.http import JsonResponse
#from habitaciones.forms import RegisterFormModel
from habitaciones.forms import RegisterForm
from habitaciones.models import Habitaciones
from hoteles2.models import Hoteles
from django.views.generic.list import ListView
# Create your views here.

def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        data = form.cleaned_data
        data2= Hoteles.objects.get(id=3)

        habitacion = Habitaciones.objects.create(
                piso=data['piso'],
                numero=data['numero'],
                costo_x_dia=data['costo'],
                capacidad=data['capacidad'],
                id_hotel_id=data2
                )

        return JsonResponse({
                            'piso' : habitacion.piso,
                            'numero' : habitacion.numero,
                            'costo' : habitacion.costo_x_dia,
                            'capacidad' : habitacion.capacidad,
                            'Id hotel' : habitacion.id_hotel_id.id

                            })
    return render(request,'habitaciones/habitaciones.html',{'form':form})
