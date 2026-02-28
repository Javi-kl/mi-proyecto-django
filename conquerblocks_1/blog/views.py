from django.shortcuts import render


# Vistas generales de la aplicación
def blog_list(request):
    return render(request, "blog/blog_list.html")


def blog_detail(request, id):
    return render(request, "blog/blog_detail.html")
