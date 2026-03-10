from django import forms


class ContactForm(forms.Form):
    nombre = forms.CharField(max_length=50, label="Nombre")
    email = forms.EmailField(label="Email")
    comentario = forms.CharField(
        max_length=2000, label="Comentario", widget=forms.Textarea
    )

    def clean_name(self):
        nombre = self.cleaned_data.get("nombre")
        if len(nombre) < 5:
            raise forms.ValidationError("El nombre debe tener al menos 5 caracteres")
        return nombre


class LoginForm(forms.Form):
    username = forms.CharField(max_length=140, label="Nombre de usuario")
    password = forms.CharField(widget=forms.PasswordInput(), label="Contraseña")
