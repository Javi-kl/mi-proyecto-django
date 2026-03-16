from django.contrib import admin

# Register your models here.
from .models import PostModel


@admin.register(PostModel)
class PostResource(admin.ModelAdmin):
    model = PostModel
    list_display = ("pk", "title", "autor", "created_at")
