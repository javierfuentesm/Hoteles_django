from django.shortcuts import render
from django.http import JsonResponse
#from habitaciones.forms import RegisterFormModel
from habitaciones.forms import RegisterForm
from habitaciones.models import Habitaciones
# Create your views here.

def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        data = form.cleaned_data
        habitacion = Habitaciones.objects.create(
                piso=data['piso'],
                numero=data['numero'],
                costo_x_dia=data['costo'],
                capacidad=data['capacidad'],
                id_hotel_id=data['idhotel']
                )

        return JsonResponse({
                            'piso' : habitacion.piso,
                            'numero' : habitacion.data,
                            'costo' : habitacion.costo_x_dia,
                            'capacidad' : habitacion.capacidad,
                            'Id hotel' : habitacion.id_hotel_id
        
                            })
    return render(request,'habitaciones/habitaciones.html',{'form':form})
