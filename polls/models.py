from django.db import models
#from django.contrib.auth.models import AbstractBaseUser

# Create your models here.

"""class User(AbstractBaseUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", 'Admin'
        USER = "USER", 'User'

    base_role = Role.USER
"""


class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.FloatField()
    descripcion = models.CharField(max_length=200)

"""
class Category(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
"""
