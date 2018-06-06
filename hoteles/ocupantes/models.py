from django.db import models


class Ocupantes (models.Model):
    id_habitacion_id =models.ForeignKey('habitaciones.Habitaciones',on_delete=models.CASCADE)
    id_huesped_id =models.ForeignKey('huespedes.Huespedes',on_delete=models.CASCADE)
