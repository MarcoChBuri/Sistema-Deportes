from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from Persona.models import Deportista
from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver

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

    def __str__(self):
        return self.nombre

@receiver(m2m_changed, sender=Equipo.participantes.through)
def validate_participantes(sender, instance, action, **kwargs):
    if action == "post_add" or action == "post_remove" or action == "post_clear":
        if instance.participantes.count() > 11:
            raise ValidationError("No puedes tener más de 11 participantes en un equipo")

@receiver(post_save, sender=Equipo)
def update_nr_participantes(sender, instance, **kwargs):
    instance.nr_participantes = instance.participantes.count()
    instance.save()
