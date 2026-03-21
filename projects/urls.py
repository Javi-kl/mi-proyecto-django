from django.urls import path

from .views import (
    ProjectCreateView,
    ProjectDeleteView,
    ProjectDetailView,
    ProjectListView,
    ProjectUpdateView,
)

app_name = "projects"

urlpatterns = [
    path("lista/", ProjectListView.as_view(), name="projects_list"),
    path("lista/detalle/<int:pk>", ProjectDetailView.as_view(), name="project_detail"),
    path("create/", ProjectCreateView.as_view(), name="project_create"),
    path("update/<int:pk>", ProjectUpdateView.as_view(), name="project_update"),
    path("delete/<int:pk>", ProjectDeleteView.as_view(), name="project_delete"),
]
