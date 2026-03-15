from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView

from .forms import PostModelFormCreate
from .models import Post


def blog_create(request):
    if request.method == "POST":
        form = PostModelFormCreate(request.POST)
        if form.is_valid():
            form.save()
            context = {"msj": "Noticia creada correctamente"}
            return redirect("blog:blog_list")

        else:
            context = {"form": form, "error": True}
            return render(request, "blog/blog_create.html", context)
    else:
        form = PostModelFormCreate()
        context = {"form": form}
        return render(request, "blog/blog_create.html", context)


class PostListView(ListView):
    model = Post
    template_name = "blog/posts_list_ccbv.html"
    context_object_name = "posts"


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/posts_detail_ccbv.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context["titulo"] = "Noticia completa"
        return context
