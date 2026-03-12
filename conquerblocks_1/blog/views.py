from django.shortcuts import redirect, render

from .forms import PostModelFormCreate
from .models import Post


# Vistas generales de la aplicación
def blog_list(request):
    all_posts = Post.objects.all()
    context = {"posts": all_posts}
    return render(request, "blog/blog_list.html", context)


def blog_detail(request, id):
    post = Post.objects.get(pk=id)
    context = {"post": post}
    return render(request, "blog/blog_detail.html", context)


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
