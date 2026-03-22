from django.contrib import admin

from .models import ProjectModel


@admin.register(ProjectModel)
class ProjectResource(admin.ModelAdmin):
    model = ProjectModel
    list_display = ("pk", "title", "order", "created_at")
    ordering = ("order", "created_at")
    editable_list = ["order"]
