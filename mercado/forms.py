from django import forms

class PublicarAutoForm(forms.Form):
    MARCAS = sorted([
        "Volkswagen", "Audi", "Ford", "Chevrolet", "Honda", "Toyota", 
        "Hyundai", "Suzuki", "Lexus", "DS", "Mercedes-Benz", "Nissan", 
        "Fiat", "Ferrari", "Lamborghini", "Tesla", "Chrysler", "BMW", 
        "Jeep", "Citroën", "Peugeot", "Renault", "RAM", "Coradir", 
        "Bugatti", "Porsche", "Corvette", "McLaren"
    ])

    marca = forms.ChoiceField(choices=[(marca, marca) for marca in MARCAS], widget=forms.Select(attrs={'class': 'form-control'}))
    modelo = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    ano = forms.IntegerField(min_value=1910, max_value=2024, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    kilometros = forms.IntegerField(min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    MONEDAS = [('ARS', 'ARS'), ('USD', 'USD')]
    moneda = forms.ChoiceField(choices=MONEDAS, widget=forms.Select(attrs={'class': 'form-control'}))
    precio = forms.DecimalField(min_value=0, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    imagen = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))
    descripcion = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))


from django.shortcuts import render, redirect
from .forms import PublicarAutoForm

def publicar(request):
    if request.method == 'POST':
        form = PublicarAutoForm(request.POST, request.FILES)
        if form.is_valid():
            return redirect('mercado:inicio')
    else:
        form = PublicarAutoForm()
    return render(request, 'mercado/publicar.html', {'form': form})
