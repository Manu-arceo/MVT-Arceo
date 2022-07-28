from django.db import models

# Create your models here.
class padres(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    fechaDeNacimiento = models.DateField()
    edad = models.IntegerField()
    ocupacion = models.CharField(max_length=30)
  

class hermanos(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    fechaDeNacimiento = models.DateField()
    edad = models.IntegerField()
    ocupacion = models.CharField(max_length=30)
 