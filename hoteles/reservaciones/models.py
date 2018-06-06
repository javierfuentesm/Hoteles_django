from django.db import models


class Reservaciones (models.Model):

    fecha_inicia=models.DateField()
    fecha_final=models.DateField()
    costo_total=models.IntegerField(max_length=11)
    reservaciones_id_habitacion=models.ManyToManyField('habitaciones.Habitaciones')
