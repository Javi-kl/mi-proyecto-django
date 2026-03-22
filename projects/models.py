from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from thumbnails.fields import ImageField


class ProjectModel(models.Model):
    title = models.CharField(verbose_name="Título", max_length=200)
    description = RichTextField(verbose_name="Descripción")
    created_at = models.DateTimeField(
        verbose_name="Fecha y hora de creación", default=timezone.now
    )

    project_img = ImageField(
        verbose_name="Imagen del proyecto",
        upload_to="projects/images/",
        null=True,
        blank=True,
    )
    github_url = models.URLField(verbose_name="GitHub", blank=True, null=True)

    created_by = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.SET_NULL
    )

    order = models.PositiveIntegerField(verbose_name="Orden", default=0, blank=True)

    class Meta:
        ordering = ["-order", "-created_at"]
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"

    def __str__(self) -> str:
        return self.title
