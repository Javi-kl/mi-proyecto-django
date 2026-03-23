from projects.models import ProjectModel


def get_statistics_projects(request):
    return {"n_projects": ProjectModel.objects.all().count}


def get_avatar(request):
    return {"site_avatar": "/static/img/avatar.jpeg"}
