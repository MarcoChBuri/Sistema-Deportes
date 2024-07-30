from django.db import models
class Datos (models.Model):
    nombre = models.CharField(max_length=100)
    nroEquipo = models.IntegerField()
    def __str__(self):
        return self.nombre


