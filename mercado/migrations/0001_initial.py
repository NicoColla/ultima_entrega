# Generated by Django 5.0.4 on 2024-06-12 22:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('SUV', 'SUV'), ('Hatchback', 'Hatchback'), ('Sedan', 'Sedan'), ('Descapotable', 'Descapotable'), ('Coupé', 'Coupé'), ('Familiar', 'Familiar'), ('Utilitario', 'Utilitario'), ('Pick-Up', 'Pick-Up'), ('Naked', 'Naked'), ('Deportiva', 'Deportiva'), ('Doble propósito', 'Doble propósito'), ('Cross', 'Cross'), ('Custom', 'Custom'), ('Scrambler', 'Scrambler'), ('Scooter', 'Scooter'), ('Touring', 'Touring')], max_length=20)),
                ('marca', models.CharField(choices=[('Volkswagen', 'Volkswagen'), ('Audi', 'Audi'), ('Ford', 'Ford'), ('Chevrolet', 'Chevrolet'), ('Honda', 'Honda'), ('Toyota', 'Toyota'), ('Hyundai', 'Hyundai'), ('Suzuki', 'Suzuki'), ('Lexus', 'Lexus'), ('DS', 'DS'), ('Mercedes-Benz', 'Mercedes-Benz'), ('Nissan', 'Nissan'), ('Fiat', 'Fiat'), ('Ferrari', 'Ferrari'), ('Lamborghini', 'Lamborghini'), ('Tesla', 'Tesla'), ('Chrysler', 'Chrysler'), ('BMW', 'BMW'), ('Jeep', 'Jeep'), ('Citroën', 'Citroën'), ('Peugeot', 'Peugeot'), ('Renault', 'Renault'), ('RAM', 'RAM'), ('Coradir', 'Coradir'), ('Bugatti', 'Bugatti'), ('Porsche', 'Porsche'), ('Corvette', 'Corvette'), ('McLaren', 'McLaren'), ('Yamaha', 'Yamaha'), ('Zanella', 'Zanella'), ('Kawasaki', 'Kawasaki'), ('Motomel', 'Motomel'), ('Harley-Davidson', 'Harley-Davidson'), ('Triumph', 'Triumph'), ('Ducati', 'Ducati')], max_length=20)),
                ('modelo', models.CharField(max_length=100)),
                ('ano', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='VentaVehiculo',
            fields=[
                ('vehiculo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mercado.vehiculo')),
                ('kilometros', models.IntegerField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('imagen', models.ImageField(upload_to='vehiculos/')),
                ('descripcion', models.TextField()),
            ],
            bases=('mercado.vehiculo',),
        ),
    ]