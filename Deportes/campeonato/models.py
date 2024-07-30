from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from Persona.models import Deportista

class Campeonato(models.Model):
    nombre = models.CharField(max_length=100)
    equipo = models.CharField(max_length=100)
    deportista = models.ForeignKey(Deportista, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    participantes = models.ManyToManyField(Deportista)
    disiplina = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    nr_participantes = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(11)])

    def save(self, *args, **kwargs):
        if self.participantes.count() > 11:
            raise ValidationError("No puedes tener más de 11 participantes en un equipo")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre