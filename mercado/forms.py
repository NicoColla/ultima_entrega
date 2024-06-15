from django import forms
from .models import VentaVehiculo, Precio, MONEDAS

class PrecioField(forms.MultiValueField):
    def __init__(self, *args, **kwargs):
        fields = (
            forms.DecimalField(max_digits=10, decimal_places=2),
            forms.ChoiceField(choices=[(moneda, moneda) for moneda in MONEDAS]),
        )
        super().__init__(fields, *args, **kwargs)

    def compress(self, data_list):
        if data_list:
            valor, moneda = data_list
            return Precio.get_or_create(moneda=moneda, valor=valor)
        return None

class PublicarAutoForm(forms.ModelForm):
    precio = PrecioField()

    class Meta:
        model = VentaVehiculo
        fields = ['tipo', 'marca', 'modelo', 'año', 'kilometros', 'precio', 'color', 'imagen', 'descripcion']
        widgets = {
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'marca': forms.Select(attrs={'class': 'form-control'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'año': forms.NumberInput(attrs={'class': 'form-control'}),
            'kilometros': forms.NumberInput(attrs={'class': 'form-control'}),
            'color': forms.Select(attrs={'class': 'form-control'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.precio = self.cleaned_data['precio']
        if commit:
            instance.save()
        return instance
