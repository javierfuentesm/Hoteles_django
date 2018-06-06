from django.db import models


class Habitaciones (models.Model):

    piso=models.IntegerField(max_length=11)
    numero=models.IntegerField(max_length=11)
    costo_x_dia=models.IntegerField(max_length=11)
    capacidad=models.IntegerField(max_length=11)
    id_hotel_id=models.ForeignKey('hoteles2.Hoteles',on_delete=models.CASCADE)
