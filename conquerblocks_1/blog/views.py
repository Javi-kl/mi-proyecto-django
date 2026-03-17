from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .models import PostModel


class PostCreateView(LoginRequiredMixin, CreateView):
    model = PostModel
    fields = ["title", "content", "show_home", "blog_img"]
    template_name = "blog/post_create.html"
    success_url = reverse_lazy("blog:posts_list")

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)


class PostListView(LoginRequiredMixin, ListView):
    model = PostModel
    template_name = "blog/posts_list.html"
    context_object_name = "posts"


class PostDetailView(LoginRequiredMixin, DetailView):
    model = PostModel
    template_name = "blog/post_detail.html"
    context_object_name = "post"


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = PostModel
    fields = ["title", "content", "show_home", "blog_img"]
    template_name = "blog/post_update.html"
    success_url = reverse_lazy("blog:posts_list")


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = PostModel
    success_url = reverse_lazy("blog:posts_list")
    template_name = "blog/post_delete.html"
