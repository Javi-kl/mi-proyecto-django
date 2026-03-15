from django.urls import path

from .views import (
    AboutView,
    ContactFormView,
    home,
    login_view,
    logout_view,
    register,
)

app_name = "core"
urlpatterns = [
    path("", home, name="home"),
    path("sobre-nosotros/", AboutView.as_view(), name="about_us"),
    path("contacto/", ContactFormView.as_view(), name="contact"),
    path("registro/", register, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
]
