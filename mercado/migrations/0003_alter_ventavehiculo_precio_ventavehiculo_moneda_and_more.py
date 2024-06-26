# Generated by Django 5.0.4 on 2024-06-16 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mercado', '0002_precio_rename_ano_vehiculo_año_ventavehiculo_color_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ventavehiculo',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=100),
        ),
        migrations.AddField(
            model_name='ventavehiculo',
            name='moneda',
            field=models.CharField(choices=[('ARS', 'Pesos Argentinos'), ('USD', 'Dólares Americanos')], default='ARS', max_length=3),
        ),
        migrations.DeleteModel(
            name='Precio',
        ),
    ]
