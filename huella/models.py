from django.db import models
#para los signals
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    cedula = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)

class Traza(models.Model):
    nombre = models.CharField(max_length=50)
    nombre_id = models.CharField(max_length=50)
    fecha = models.DateTimeField(auto_now=True)
