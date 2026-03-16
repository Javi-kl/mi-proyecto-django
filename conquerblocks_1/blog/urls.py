from django.urls import path

from .views import (
    PostCreateView,
    PostDeleteView,
    PostDetailView,
    PostListView,
    PostUpdateView,
)

app_name = "blog"


urlpatterns = [
    path("lista/", PostListView.as_view(), name="posts_list"),
    path("lista/detalle/<pk>", PostDetailView.as_view(), name="post_detail"),
    path("create/", PostCreateView.as_view(), name="post_create"),
    path("update/<pk>", PostUpdateView.as_view(), name="post_update"),
    path("delete/<pk>", PostDeleteView.as_view(), name="post_delete"),
]
