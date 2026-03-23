from django.contrib import admin

from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("pk", "email", "created_at", "contactado")
    list_filter = ("contactado", "created_at")
    search_fields = ("email", "comentario")
    readonly_fields = ("created_at",)
    ordering = ("-created_at",)
