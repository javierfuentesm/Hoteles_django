from django.shortcuts import render
from django.http import JsonResponse
from hoteles2.forms import RegisterFormModel
from hoteles2.models import Hoteles
# Create your views here.

def register(request):
    form = RegisterFormModel(request.POST or None)
    if form.is_valid():
        hotel = form.save()

        return JsonResponse({
                            'El id del hotel es ' :hotel.id,
                            'El nombre del Hotel es' : hotel.nombre,
                            'La calificacion es' : hotel.calificacion

                            })
    return render(request,'hoteles2/hoteles.html',{'form':form})
