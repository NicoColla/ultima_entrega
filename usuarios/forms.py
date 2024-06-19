from django import forms
from .models import Usuario
from django.core.exceptions import ValidationError 
import re

class RegistroForm(forms.ModelForm):
    contrasena = forms.CharField(widget=forms.PasswordInput, min_length=8, max_length=24, label="Contraseña")
    confirmar_contrasena = forms.CharField(widget=forms.PasswordInput, label="Confirmar Contraseña")
    telefono = forms.CharField(min_length=10, max_length=10, required=False, label="Teléfono / Whatsapp")

    DIAS = [(str(i), str(i)) for i in range(1, 32)]
    MESES = [(str(i), str(i)) for i in range(1, 13)]
    ANOS = [(str(i), str(i)) for i in range(1900, 2007)]

    dia_nacimiento = forms.ChoiceField(choices=DIAS, label="Día")
    mes_nacimiento = forms.ChoiceField(choices=MESES, label="Mes")
    ano_nacimiento = forms.ChoiceField(choices=ANOS, label="Año")

    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'email', 'telefono', 'dia_nacimiento', 'mes_nacimiento', 'ano_nacimiento']
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo Electrónico',
            'telefono': 'Teléfono / Whatsapp',
            'dia_nacimiento': 'Día de Nacimiento',
            'mes_nacimiento': 'Mes de Nacimiento',
            'ano_nacimiento': 'Año de Nacimiento',
        }
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_pattern = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w{2,3}$')
        if email and not email_pattern.match(email):
            raise forms.ValidationError("El correo electrónico debe tener un formato válido y terminar en '.com'")
        return email
    
    def clean(self):
        cleaned_data = super().clean()
        contrasena = cleaned_data.get('contrasena')
        confirmar_contrasena = cleaned_data.get('confirmar_contrasena')

        dia = cleaned_data.get('dia_nacimiento')
        mes = cleaned_data.get('mes_nacimiento')
        ano = cleaned_data.get('ano_nacimiento')

        if dia and mes and ano:
            try:
                fecha_nacimiento = f"{ano}-{mes}-{dia}"
                cleaned_data['fecha_nacimiento'] = fecha_nacimiento
            except ValueError:
                raise forms.ValidationError("La fecha de nacimiento no es válida")

        if contrasena and confirmar_contrasena and contrasena != confirmar_contrasena:
            raise forms.ValidationError("Las contraseñas no coinciden")

        if contrasena and not any(char.isdigit() for char in contrasena):
            raise forms.ValidationError("La contraseña debe contener al menos un número")

        return cleaned_data


class LoginForm(forms.Form):
    email = forms.EmailField()
    contrasena = forms.CharField(widget=forms.PasswordInput)
