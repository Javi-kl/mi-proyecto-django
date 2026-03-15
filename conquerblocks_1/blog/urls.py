from django.urls import path

from .views import (
    PostDetailView,
    PostListView,
    blog_create,
)

app_name = "blog"


urlpatterns = [
    path("lista/", PostListView.as_view(), name="posts_list_ccbv"),
    path("lista/detalle/<pk>", PostDetailView.as_view(), name="posts_detail_ccbv"),
    path("create/", blog_create, name="blog_create"),
]
