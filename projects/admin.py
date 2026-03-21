from django.contrib import admin

from .models import ProjectModel


@admin.register(ProjectModel)
class ProjectResource(admin.ModelAdmin):
    model = ProjectModel
    list_display = ("pk", "title", "created_at")
