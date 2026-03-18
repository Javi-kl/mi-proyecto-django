from django.forms import ModelForm

from .models import PostModel


class PostModelFormCreate(ModelForm):
    class Meta:
        model = PostModel
        fields = ["title", "content", "created_at", "show_home", "blog_img"]
