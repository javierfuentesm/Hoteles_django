from django.db import models


class Reservaciones (models.Model):

    fecha_inicia=models.DateField()
    fecha_final=models.DateField()
    costo_total=models.IntegerField(mx_length=11)
