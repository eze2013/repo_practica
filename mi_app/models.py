from django.db import models

class Curso (models.Model):

    nombre = models.CharField(max_length=40)  # como en base de datos pide un tipo de dato y su longitud
    camada = models.IntegerField() # este es para campos numericos enteros


