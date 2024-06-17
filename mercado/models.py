from django.db import models
from usuarios.models import Usuario

MARCAS = [
    "Volkswagen", "Audi", "Ford", "Chevrolet", "Honda", "Toyota",
    "Hyundai", "Suzuki", "Lexus", "DS", "Mercedes-Benz", "Nissan",
    "Fiat", "Ferrari", "Lamborghini", "Tesla", "Chrysler", "BMW",
    "Jeep", "Citroën", "Peugeot", "Renault", "RAM", "Coradir",
    "Bugatti", "Porsche", "Corvette", "McLaren", "Yamaha", "Zanella",
    "Kawasaki", "Motomel", "Harley-Davidson", "Triumph", "Ducati"
]

TIPOS = [
    "SUV", "Hatchback", "Sedan", "Descapotable", "Coupé", "Familiar", "Utilitario", "Pick-Up", "Naked", "Deportiva",
    "Doble propósito", "Cross", "Custom", "Scrambler", "Scooter", "Touring"
]

COLORES = [
    "Blanco", "Gris claro", "Gris oscuro", "Negro", "Rojo", "Granate", "Azul", "Verde"
]

MONEDAS = [
    ("ARS", "ARS"), ("USD", "USD")
]

class Vehiculo(models.Model):
    tipo = models.CharField(max_length=20, choices=[(tipo, tipo) for tipo in TIPOS])
    marca = models.CharField(max_length=20, choices=[(marca, marca) for marca in MARCAS])
    modelo = models.CharField(max_length=100)
    año = models.IntegerField()

    def __str__(self):
        return f"{self.tipo} {self.marca} {self.modelo} ({self.año})"

class VentaVehiculo(Vehiculo):
    vendedor = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, blank=True)
    kilometros = models.IntegerField()
    precio = models.DecimalField(max_digits=100, decimal_places=2)
    moneda = models.CharField(max_length=3, choices=MONEDAS, default="ARS")
    color = models.CharField(max_length=20, choices=[(color, color) for color in COLORES], default="Negro")
    imagen = models.ImageField(upload_to='media/vehiculos/')
    descripcion = models.TextField()

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.año}) - {self.precio} {self.moneda}"