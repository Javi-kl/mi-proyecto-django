from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from thumbnails.fields import ImageField


# Create your models here.
class PostModel(models.Model):
    title = models.CharField(verbose_name="Título", max_length=200)
    content = RichTextField(verbose_name="Contenido")
    created_at = models.DateTimeField(
        verbose_name="Fecha y hora de creacion", default=timezone.now
    )
    show_home = models.BooleanField("Mostrar en la home", default=False)

    blog_img = ImageField(
        verbose_name="Portada del blog",
        upload_to="blog/images/",
        null=True,
        blank=True,
    )
    created_by = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.SET_NULL
    )

    def __str__(self) -> str:
        return self.title
