from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
        labels = {"content": ""}
        widgets = {
            "content": forms.Textarea(
                attrs={
                    "rows": 4,
                    "class": "form-control",
                    "placeholder": "Escribe tu comentario...",
                    "maxlength": 1000,
                }
            ),
        }

    def clean_content(self):
        content = self.cleaned_data.get("content", "")
        content = content.strip()
        if len(content) < 3:
            raise forms.ValidationError(
                "El comentario debe tener al menos 3 caracteres."
            )
        if len(content) > 1000:
            raise forms.ValidationError(
                "El comentario no puede exceder 1000 caracteres."
            )
        return content
