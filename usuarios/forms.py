from django import forms
from .models import Usuario

class RegistroForm(forms.ModelForm):
    contrasena = forms.CharField(widget=forms.PasswordInput, min_length=8, label="Contraseña")
    confirmar_contrasena = forms.CharField(widget=forms.PasswordInput, label="Confirmar Contraseña")
    telefono = forms.CharField(max_length=15, required=False, label="Teléfono / Whatsapp")

    DIAS = [(str(i), str(i)) for i in range(1, 32)]
    MESES = [(str(i), str(i)) for i in range(1, 13)]
    ANOS = [(str(i), str(i)) for i in range(1900, 2007)]

    dia_nacimiento = forms.ChoiceField(choices=DIAS, label="Día")
    mes_nacimiento = forms.ChoiceField(choices=MESES, label="Mes")
    ano_nacimiento = forms.ChoiceField(choices=ANOS, label="Año")

    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'email', 'telefono']
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo Electrónico',
            'telefono': 'Teléfono / Whatsapp',
        }

    def clean(self):
        cleaned_data = super().clean()
        contrasena = cleaned_data.get('contrasena')
        confirmar_contrasena = cleaned_data.get('confirmar_contrasena')

        if contrasena and confirmar_contrasena and contrasena != confirmar_contrasena:
            raise forms.ValidationError("Las contraseñas no coinciden")

        if contrasena and not any(char.isdigit() for char in contrasena):
            raise forms.ValidationError("La contraseña debe contener al menos un número")

        return cleaned_data


class LoginForm(forms.Form):
    email = forms.EmailField()
    contrasena = forms.CharField(widget=forms.PasswordInput)
