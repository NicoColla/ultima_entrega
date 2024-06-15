from django.db import models

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

class Vehiculo(models.Model):
    tipo = models.CharField(max_length=20, choices=[(tipo, tipo) for tipo in TIPOS])
    marca = models.CharField(max_length=20, choices=[(marca, marca) for marca in MARCAS])
    modelo = models.CharField(max_length=100)
    año = models.IntegerField()

    def __str__(self):
        return f"{self.tipo} {self.marca} {self.modelo} ({self.año})"

class VentaVehiculo(Vehiculo):
    kilometros = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=20, choices=[(color, color) for color in COLORES])
    imagen = models.ImageField(upload_to='vehiculos/')
    descripcion = models.TextField()

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.año}) - ${self.precio}"
