from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import FormView, TemplateView

from blog.models import PostModel

from .forms import ContactForm, LoginForm, UserRegisterForm
from .models import Contact


# Vistas generales de la aplicación
def home(request):
    context = {
        "posts": PostModel.objects.filter(show_home=True),
    }
    return render(request, "core/home.html", context)


class AboutView(TemplateView):
    template_name = "core/about_view.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context["titulo"] = "Sobre mí"
        return context


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
    if request.POST:
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            password1 = form.cleaned_data["password1"]
            password2 = form.cleaned_data["password2"]

            user = User.objects.create_user(username, email, password1)

            if user:
                user.first_name = first_name
                user.last_name = last_name
                user.save()

            context = {"msj": "Usuario creado correctamente"}
            return render(request, "core/register.html", context)
        else:
            context = {"form": form, "error": True}
            return render(request, "core/register.html", context)
    else:
        form = UserRegisterForm()
        context = {"form": form}
        return render(request, "core/register.html", context)


class ContactFormView(FormView):
    template_name = "core/contact.html"
    form_class = ContactForm
    success_url = "/"

    def form_valid(self, form):
        nombre = form.cleaned_data["nombre"]
        email = form.cleaned_data["email"]
        comentario = form.cleaned_data["comentario"]

        Contact.objects.create(nombre=nombre, email=email, comentario=comentario)

        message_content = (
            f"{nombre} con email {email} ha escrito lo siguiente: {comentario}"
        )
        # NO OPERATIVA
        success = send_mail(
            "Formulario de contacto",
            message_content,
            "info@laveladaconquer.com",
            ["prueba@gmail.com"],
            fail_silently=False,
        )
        return super().form_valid(form)
