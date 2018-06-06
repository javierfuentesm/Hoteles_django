from django.shortcuts import render
from django.http import JsonResponse
from habitaciones.forms import RegisterFormModel
# Create your views here.

def register(request):
    form = RegisterFormModel(request.POST or None)
    if form.is_valid():
        habitacion = form.save()

        return JsonResponse({
                            'piso' : habitacion.piso,
                            'numero' : habitacion.numero,
                            'costo' : habitacion.costo_x_dia,
                            'capacidad' : habitacion.capacidad,
                            'Id hotel' : habitacion.id_hotel_id.id

                            })
    return render(request,'habitaciones/habitaciones.html',{'form':form})
