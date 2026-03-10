from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse

from blog.models import Post
from courses.models import Course

from .forms import ContactForm, LoginForm
from .models import Contact


# Vistas generales de la aplicación
def home(request):
    context = {
        "courses": Course.objects.filter(show_home=True),
        "posts": Post.objects.filter(show_home=True),
    }
    return render(request, "core/home.html", context)


def about_us(request):
    return render(request, "core/about_us.html")


def login_view(request):
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse("core:home"))
            else:
                context = {
                    "form": form,
                    "error": True,
                    "error_message": "Usuario no válido",
                }
                return render(request, "core/login.html", context)
        else:
            context = {"form": form, "error": True}
            return render(request, "core/login.html", context)
    else:
        form = LoginForm()
        context = {"form": form}
        return render(request, "core/login.html", context)


def logout_view(request):
    logout(request)
    return redirect(reverse("core:home"))


def register(request):
    return render(request, "core/register.html")


def contact(request):
    if request.POST:
        formulario = ContactForm(request.POST)
        if formulario.is_valid():
            nombre = formulario.cleaned_data["nombre"]
            email = formulario.cleaned_data["email"]
            comentario = formulario.cleaned_data["comentario"]

            Contact.objects.create(nombre=nombre, email=email, comentario=comentario)

            message_content = (
                f"{nombre} con email {email} ha escrito lo siguiente: {comentario}"
            )
            success = send_mail(
                "Formulario de contacto",
                message_content,
                "info@laveladaconquer.com",
                ["prueba@gmail.com"],
                fail_silently=False,
            )
            context = {"form": formulario, "success": success}
            return render(request, "core/contact.html", context)

        else:
            context = {"form": formulario}
            return render(request, "core/contact.html", context)

    formulario = ContactForm()
    context = {"form": formulario}

    return render(request, "core/contact.html", context)
