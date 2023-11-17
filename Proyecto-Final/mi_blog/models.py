
# Create your models here.
from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    apellido = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.apellido} ,({self.nombre}), {self.fecha_nacimiento}"

class Familiares(Persona):
    parentesco = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.apellido}, {self.nombre}, {self.parentesco}"
    

class Amigos(Persona):
    nivel_amistad = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.apellido}, {self.nombre}, {self.nivel_amistad}"

class Viajes(models.Model):
    destino = models.CharField(max_length=100)
    duracion = models.IntegerField()
    fecha_viaje = models.DateField()
    viajeros = models.ManyToManyField(Persona)

    def __str__(self):
        return f"{self.destino}, {self.fecha_viaje}, {self.viajeros},{self.duracion}"



    