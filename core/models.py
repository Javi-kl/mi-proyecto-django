from django.db import models
from django.utils import timezone


class Contact(models.Model):
    nombre = models.CharField(
        verbose_name="nombre", max_length=50, blank=True, null=True
    )
    email = models.EmailField(verbose_name="email")
    comentario = models.TextField(verbose_name="comentario")
    created_at = models.DateTimeField(
        verbose_name="Fecha y hora de creación", default=timezone.now
    )
    contactado = models.BooleanField(
        verbose_name="¿Se ha contactado con él?", default=False
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Mensaje de contacto"
        verbose_name_plural = "Mensajes de contacto"

    def __str__(self):
        return f"{self.email} - {self.created_at.strftime('%d/%m/%Y')}"
