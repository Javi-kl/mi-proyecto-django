from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .models import PostModel


class PostCreateView(CreateView):
    model = PostModel
    fields = ["title", "content", "autor", "show_home", "blog_img"]
    template_name = "blog/post_create.html"
    success_url = reverse_lazy("blog:posts_list")


class PostListView(ListView):
    model = PostModel
    template_name = "blog/posts_list.html"
    context_object_name = "posts"


class PostDetailView(DetailView):
    model = PostModel
    template_name = "blog/post_detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context["titulo"] = "Noticia completa"
        return context


class PostUpdateView(UpdateView):
    model = PostModel
    fields = ["title", "content", "autor", "show_home", "blog_img"]
    template_name = "blog/post_update.html"
    success_url = reverse_lazy("blog:posts_list")


class PostDeleteView(DeleteView):
    model = PostModel
    success_url = reverse_lazy("blog:posts_list")
    template_name = "blog/post_delete.html"
