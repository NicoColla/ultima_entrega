# Generated by Django 5.0.4 on 2024-06-16 21:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mercado', '0003_alter_ventavehiculo_precio_ventavehiculo_moneda_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='ventavehiculo',
            name='vendedor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ventavehiculo',
            name='imagen',
            field=models.ImageField(upload_to='media/vehiculos/'),
        ),
        migrations.AlterField(
            model_name='ventavehiculo',
            name='moneda',
            field=models.CharField(choices=[('ARS', 'ARS'), ('USD', 'USD')], default='ARS', max_length=3),
        ),
    ]
