from django.db import models

class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=100, unique=True)
    contraseña = models.CharField(max_length=100)
    correo_electronico = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre_usuario

# Create your models here.
