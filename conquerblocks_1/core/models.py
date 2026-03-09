from django.db import models
from django.utils import timezone


# Create your models here.
class Contact(models.Model):
    nombre = models.CharField(verbose_name="nombre", max_length=50)
    email = models.EmailField(verbose_name="email")
    comentario = models.TextField(verbose_name="comentario que ha dejado en web")
    created_at = models.DateTimeField(
        verbose_name="Fecha y hora de creacion", default=timezone.now
    )
    contactado = models.BooleanField(
        verbose_name="¿Se ha contactado con él?", default=False
    )


def __str__(self):
    return self.nombre
