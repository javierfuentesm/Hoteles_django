from django.db import models


class Hoteles (models.Model):
    nombre=models.CharField(max_length=100)
    calificacion=models.IntegerField(max_length=100)
