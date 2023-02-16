from django.db import models

# Create your models here.
class Equipo(models.Model):
    nombre = models.CharField(max_length=40)
    provincia = models.CharField(max_length=40)

    def __str__(self):
        return self.nombre + ' (' + str(self.provincia) + ')'

class Jugador(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    peso = models.FloatField()
    altura = models.FloatField()
    equipo = models.CharField(max_length=40)

    def __str__(self):
        return self.nombre + ' ' + str(self.apellido)

class Entrenador(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    equipo = models.CharField(max_length=40)

    def __str__(self):
        return self.nombre + ' ' + str(self.apellido) + ' (' + (self.equipo) + ')'

class Arbitro(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    nacionalidad = models.CharField(max_length=40)
    
    def __str__(self):
        return self.nombre + ' ' + str(self.apellido)


