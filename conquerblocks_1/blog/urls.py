from django.urls import path

from .views import (
    PostDetailView,
    PostListView,
    PruebaTemplateView,
    blog_create,
    blog_detail,
    blog_list,
)

app_name = "blog"


urlpatterns = [
    path("", blog_list, name="blog_list"),
    path("lista/", PostListView.as_view(), name="posts_list_ccbv"),
    path("lista/detalle/<pk>", PostDetailView.as_view(), name="posts_detail_ccbv"),
    path("<int:id>/", blog_detail, name="blog_detail"),
    path("create/", blog_create, name="blog_create"),
    path("prueba_titulo/", PruebaTemplateView.as_view(), name="title_check"),
]
