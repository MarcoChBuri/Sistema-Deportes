from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.CharField(max_length=10)
    numero = models.CharField(max_length=10)
    genero = models.CharField(max_length=100)
    class Meta:
        abstract = True
    def __str__(self):
        return self.nombre
class Deportista(Persona):
    disiplina = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre
class Juez(Persona):
    disiplina = models.CharField(max_length=100)
    def eliminarJugador(self):
        print("Eliminando jugador")
    def SancionarJugador(self):
        print("Sancionando jugador")
