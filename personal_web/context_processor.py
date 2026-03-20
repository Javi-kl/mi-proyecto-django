from blog.models import PostModel


# get_statistics_web para obtener nposts y nproyectos TODO
def get_statistics_posts(request):
    return {"n_posts": PostModel.objects.all().count}
