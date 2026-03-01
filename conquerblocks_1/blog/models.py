from django.db import models
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    title = models.CharField(verbose_name="Título", max_length=200)
    content = models.TextField(verbose_name="Contenido")
    autor = models.CharField(verbose_name="autor", max_length=100)
    created_at = models.DateTimeField(
        verbose_name="Fecha y hora de creacion", default=timezone.now
    )

    def __str__(self) -> str:
        return self.title
