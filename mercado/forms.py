from django import forms
from .models import VentaVehiculo, Comentario, Respuesta, TIPOS, MARCAS, COLORES, COMBUSTIBLE

class PublicarForm(forms.ModelForm):
    class Meta:
        model = VentaVehiculo
        fields = ['tipo', 'marca', 'modelo', 'año', 'kilometros', 'precio', 'color', 'imagen', 'descripcion', 'combustible', 'alt_combustible']
        widgets = {
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'marca': forms.Select(attrs={'class': 'form-control'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'año': forms.NumberInput(attrs={'class': 'form-control'}),
            'kilometros': forms.NumberInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'color': forms.Select(attrs={'class': 'form-control'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'combustible': forms.Select(attrs={'class': 'form-control'}),
            'alt_combustible': forms.Select(attrs={'class': 'form-control'}),
        }

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.precio = self.cleaned_data['precio']
        if commit:
            instance.save()
        return instance
    
class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']
        widgets = {
            'texto': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Escribe tu comentario aquí...'}),
        }

class RespuestaForm(forms.ModelForm):
    class Meta:
        model = Respuesta
        fields = ['texto']
        widgets = {
            'texto': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Escribí tu respuesta a...'}),
        }

class FiltroBusquedaForm(forms.Form):
    tipo = forms.ChoiceField(choices=[('', 'Todos')] + [(tipo, tipo) for tipo in TIPOS], required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    marca = forms.ChoiceField(choices=[('', 'Todas')] + [(marca, marca) for marca in MARCAS], required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    modelo = forms.ChoiceField(choices=[], required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    año = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    kilometros_max = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    color = forms.ChoiceField(choices=[('', 'Todos')] + [(color, color) for color in COLORES], required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    precio_min = forms.DecimalField(required=False, max_digits=100, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    precio_max = forms.DecimalField(required=False, max_digits=100, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    combustible = forms.ChoiceField(choices=[('', 'Todos')] + COMBUSTIBLE, required=False, widget=forms.Select(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['modelo'].choices = self.get_modelos_choices()

    def get_modelos_choices(self):
        modelos_choices = [('', 'Todos')]
        modelos_existentes = VentaVehiculo.objects.values_list('modelo', flat=True).distinct()
        for modelo in modelos_existentes:
            modelos_choices.append((modelo, modelo))
        return modelos_choices

    def actualizar_modelos(self, tipo_seleccionado, marca_seleccionada):
        modelos_choices = [('', 'Todos')]
        if tipo_seleccionado and marca_seleccionada:
            modelos_existentes = VentaVehiculo.objects.filter(tipo=tipo_seleccionado, marca=marca_seleccionada).values_list('modelo', flat=True).distinct()
        elif tipo_seleccionado:
            modelos_existentes = VentaVehiculo.objects.filter(tipo=tipo_seleccionado).values_list('modelo', flat=True).distinct()
        elif marca_seleccionada:
            modelos_existentes = VentaVehiculo.objects.filter(marca=marca_seleccionada).values_list('modelo', flat=True).distinct()
        else:
            modelos_existentes = VentaVehiculo.objects.values_list('modelo', flat=True).distinct()

        for modelo in modelos_existentes:
            modelos_choices.append((modelo, modelo))
        self.fields['modelo'].choices = modelos_choices
