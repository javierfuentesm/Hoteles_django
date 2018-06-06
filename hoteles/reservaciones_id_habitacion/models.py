from django.db import models


class Reservaciones_id_habitacion (models.Model):

    reservaciones_id =models.ForeignKey('reservaciones.Reservaciones',on_delete=models.CASCADE)
    habitaciones_id =models.ForeignKey('habitaciones.Habitaciones',on_delete=models.CASCADE)
