from blog.models import PostModel


# get_statistics_web para obtener nposts y nproyectos TODO
def get_statistics_posts(request):
    return {"n_posts": PostModel.objects.all().count}


def get_avatar(request):
    avatar_post = PostModel.objects.filter(
        blog_img__isnull=False, title="Foto perfil Thumbnails"
    ).first()
    return {"header_avatar": avatar_post}
