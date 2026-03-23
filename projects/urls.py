from django.urls import path

from .views import (
    CommentDeleteView,
    CommentUpdateView,
    ProjectCreateView,
    ProjectDeleteView,
    ProjectDetailView,
    ProjectUpdateView,
)

app_name = "projects"

urlpatterns = [
    path("<int:pk>", ProjectDetailView.as_view(), name="project_detail"),
    path("create/", ProjectCreateView.as_view(), name="project_create"),
    path("update/<int:pk>", ProjectUpdateView.as_view(), name="project_update"),
    path("delete/<int:pk>", ProjectDeleteView.as_view(), name="project_delete"),
    path("comments/<int:pk>/edit/", CommentUpdateView.as_view(), name="comment_edit"),
    path("comments/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment_delete"),
]
