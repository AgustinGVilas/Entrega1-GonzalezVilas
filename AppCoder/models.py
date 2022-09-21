from django.db import models

# Create your models here.

class Automovil(models.Model):
    
    marca = models.CharField(max_length=40)
    modelo = models.CharField(max_length=40)
    año = models.IntegerField()

class Motocicleta(models.Model):
    
    marca = models.CharField(max_length=40)
    cilindrada = models.IntegerField()
    año = models.IntegerField()

class Camion(models.Model):
    
    peso = models.IntegerField()
    capCarga = models.IntegerField()