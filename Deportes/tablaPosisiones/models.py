from django.db import models
from campeonato.models import Equipo

# Create your models here.
class TablaPosisiones(models.Model):
    equipo = models.CharField(max_length=100)
    puntos = models.IntegerField()
    partidos_jugados = models.IntegerField()
    partidos_ganados = models.IntegerField()
    partidos_empatados = models.IntegerField()
    partidos_perdidos = models.IntegerField()
    goles_favor = models.IntegerField()
    goles_contra = models.IntegerField()
    diferencia_goles = models.IntegerField()

    def __str__(self):
        return self.equipo
class Encuentro(models.Model):
    equipo_local = models.ManyToManyField(Equipo, related_name='encuentros_locales')
    equipo_visitante = models.ManyToManyField(Equipo, related_name='encuentros_visitantes')
    goles_local = models.IntegerField()
    goles_visitante = models.IntegerField()
    fecha = models.DateField()

    def __str__(self):
        return self.equipo_local + " vs " + self.equipo_visitante