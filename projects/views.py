from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
)

from .models import ProjectModel

# TODO  proteccion superuser para eliminar y actualizar proyectos


class SuperuserRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser


class ProjectCreateView(SuperuserRequiredMixin, CreateView):
    model = ProjectModel
    fields = ["title", "description", "project_img"]
    template_name = "projects/project_create.html"
    success_url = reverse_lazy("projects:projects_list")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class ProjectDetailView(DetailView):
    model = ProjectModel
    template_name = "projects/project_detail.html"
    context_object_name = "project"


class ProjectUpdateView(SuperuserRequiredMixin, UpdateView):
    model = ProjectModel
    fields = ["title", "description", "project_img"]
    template_name = "projects/project_update.html"
    success_url = reverse_lazy("projects:projects_list")


class ProjectDeleteView(SuperuserRequiredMixin, DeleteView):
    model = ProjectModel
    success_url = reverse_lazy("projects:projects_list")
    template_name = "projects/project_delete.html"
