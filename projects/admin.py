from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin

from .models import Comment, ProjectModel


@admin.register(ProjectModel)
class ProjectResource(MarkdownxModelAdmin):
    model = ProjectModel
    list_display = ("pk", "title", "order", "created_at")
    ordering = ("order", "created_at")
    editable_list = ["order"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("pk", "author", "project", "created_at", "content_preview")
    list_filter = ("created_at", "author")
    search_fields = ("content", "author__username", "project__title")
    raw_id_fields = ("project", "author")

    @admin.display(description="Contenido")
    def content_preview(self, obj):
        return obj.content[:50] + "..." if len(obj.content) > 50 else obj.content
