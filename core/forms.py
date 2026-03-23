from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["email", "comentario"]
        labels = {
            "email": "",
            "comentario": "",
        }
        widgets = {
            "comentario": forms.Textarea(
                attrs={
                    "rows": 5,
                    "class": "form-control",
                    "placeholder": "Escribe tu mensaje...",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "tu@email.com",
                }
            ),
        }

    def clean_comentario(self):
        comentario = self.cleaned_data.get("comentario", "")
        comentario = comentario.strip()
        if len(comentario) < 10:
            raise forms.ValidationError("El mensaje debe tener al menos 10 caracteres.")
        if len(comentario) > 2000:
            raise forms.ValidationError("El mensaje no puede exceder 2000 caracteres.")
        return comentario
