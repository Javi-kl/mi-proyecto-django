from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .models import ProjectModel


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = ProjectModel
    fields = ["title", "description", "show_home", "project_img"]
    template_name = "projects/project_create.html"
    success_url = reverse_lazy("projects:projects_list")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class ProjectListView(ListView):
    model = ProjectModel
    template_name = "projects/projects_list.html"
    context_object_name = "projects"


class ProjectDetailView(DetailView):
    model = ProjectModel
    template_name = "projects/project_detail.html"
    context_object_name = "project"


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = ProjectModel
    fields = ["title", "description", "show_home", "project_img"]
    template_name = "projects/project_update.html"
    success_url = reverse_lazy("projects:projects_list")


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = ProjectModel
    success_url = reverse_lazy("projects:projects_list")
    template_name = "projects/project_delete.html"
