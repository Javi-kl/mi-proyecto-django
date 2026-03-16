from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView

from .models import PostModel


class PostCreateView(CreateView):
    model = PostModel
    fields = ["title", "content", "autor", "show_home", "blog_img"]
    template_name = "blog/blog_create_ccbv.html"
    success_url = reverse_lazy("blog:posts_list_ccbv")


class PostListView(ListView):
    model = PostModel
    template_name = "blog/posts_list_ccbv.html"
    context_object_name = "posts"


class PostDetailView(DetailView):
    model = PostModel
    template_name = "blog/posts_detail_ccbv.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context["titulo"] = "Noticia completa"
        return context
