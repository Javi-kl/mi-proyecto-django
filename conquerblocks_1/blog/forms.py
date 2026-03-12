from django.forms import ModelForm

from .models import Post


class PostModelFormCreate(ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "autor", "created_at", "show_home", "blog_img"]
