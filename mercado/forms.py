from django import forms
from .models import VentaVehiculo, Comentario, Respuesta, TIPOS, MARCAS, COLORES, MONEDAS

class PublicarForm(forms.ModelForm):
    class Meta:
        model = VentaVehiculo
        fields = ['tipo', 'marca', 'modelo', 'año', 'kilometros', 'precio', 'moneda', 'color', 'imagen', 'descripcion']
        widgets = {
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'marca': forms.Select(attrs={'class': 'form-control'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'año': forms.NumberInput(attrs={'class': 'form-control'}),
            'kilometros': forms.NumberInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'moneda': forms.Select(attrs={'class': 'form-control'}),
            'color': forms.Select(attrs={'class': 'form-control'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.precio = self.cleaned_data['precio']
        instance.moneda = self.cleaned_data['moneda']
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
            'texto': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Escribe tu respuesta aquí...'}),
        }

class FiltroBusquedaForm(forms.Form):
    tipo = forms.ChoiceField(choices=[('', 'Todos')] + [(tipo, tipo) for tipo in TIPOS], required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    marca = forms.ChoiceField(choices=[('', 'Todas')] + [(marca, marca) for marca in MARCAS], required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    modelo = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    año = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    kilometros_max = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    color = forms.ChoiceField(choices=[('', 'Todos')] + [(color, color) for color in COLORES], required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    precio_min = forms.DecimalField(required=False, max_digits=100, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    precio_max = forms.DecimalField(required=False, max_digits=100, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    moneda = forms.ChoiceField(choices=[('', 'Ambas')] + [(moneda, moneda) for moneda in [m[0] for m in MONEDAS]], required=False, widget=forms.Select(attrs={'class': 'form-control'}))