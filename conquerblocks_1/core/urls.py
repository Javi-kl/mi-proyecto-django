from django.urls import path

from .views import about_us, contact, home, login, register

app_name = "core"
urlpatterns = [
    path("", home, name="home"),
    path("sobre-nosotros/", about_us, name="about_us"),
    path("contacto/", contact, name="contact"),
    path("registro/", register, name="register"),
    path("login/", login, name="login"),
]
