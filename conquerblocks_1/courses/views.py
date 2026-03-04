from django.shortcuts import render

from .models import Course


# Vistas generales de la aplicación
def course_list(request):
    all_courses = Course.objects.all()
    context = {"courses": all_courses}
    return render(request, "courses/course_list.html", context)


def course_detail(request, id):
    course = Course.objects.get(pk=id)
    context = {"course": course}
    return render(request, "courses/course_detail.html", context)
