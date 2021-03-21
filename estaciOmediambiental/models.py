from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class Usuari(AbstractUser):
    loginToken = models.TextField((""))


class Client(models.Model):
    identificador = models.TextField((""))
    localitzacio = models.TextField((""), default=None)
    quarentena = models.DateTimeField((""), auto_now=True)
    user = models.ForeignKey(
        Usuari, verbose_name=(""), on_delete=models.CASCADE, default=None, null=True)


class Sensor(models.Model):
    identificador = models.TextField((""))
    client = models.ForeignKey(
        Client, verbose_name=(""), on_delete=models.CASCADE, default=None, null=True)


class Registre(models.Model):
    hora = models.DateTimeField((""), auto_now=True)
    valor = models.TextField((""))
    sensor = models.ForeignKey(
        Sensor, verbose_name=(""), on_delete=models.CASCADE, default=None, null=True)
