from django.urls import path

from .views import about_us, contact, home, login_view, logout_view, register

app_name = "core"
urlpatterns = [
    path("", home, name="home"),
    path("sobre-nosotros/", about_us, name="about_us"),
    path("contacto/", contact, name="contact"),
    path("registro/", register, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
]
