from django.db import models


class Hoteles (models.Model):
    nombre=models.CharField(mx_length=100)
    calificacion=models.IntegerField(mx_length=100)
