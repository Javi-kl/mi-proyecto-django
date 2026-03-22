from django import forms


class ContactForm(forms.Form):
    email = forms.EmailField(label="Email")
    comentario = forms.CharField(
        max_length=2000, label="Comentario", widget=forms.Textarea
    )

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not email:
            raise forms.ValidationError("El email es requerido")
        return email
