from django.db import models


class Huespedes (models.Model):
    nombre=models.CharField(max_length=100)
    appelido_materno=models.CharField(max_length=100)
    appelido_paterno=models.CharField(max_length=100)
    reservaciones_id_huesped=models.ManyToManyField('reservaciones.Reservaciones')
