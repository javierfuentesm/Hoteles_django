from django.db import models


class Huespedes (models.Model):
    nombre=models.CharField(mx_length=100)
    appelido_materno=models.CharField(mx_length=100)
    appelido_paterno=models.CharField(mx_length=100)
