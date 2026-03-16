from django.urls import path

from .views import PostCreateView, PostDetailView, PostListView

app_name = "blog"


urlpatterns = [
    path("lista/", PostListView.as_view(), name="posts_list_ccbv"),
    path("lista/detalle/<pk>", PostDetailView.as_view(), name="posts_detail_ccbv"),
    path("create/", PostCreateView.as_view(), name="blog_create_ccbv"),
]
