# Generated by Django 4.2.6 on 2024-01-06 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flotavehicular', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flotavehicular',
            old_name='flotavehicular',
            new_name='tipovehiculo',
        ),
        migrations.AlterField(
            model_name='flotavehicular',
            name='capacidad_carga',
            field=models.CharField(help_text='Capacidad de Carga de Vehículo', max_length=20),
        ),
        migrations.AlterField(
            model_name='flotavehicular',
            name='capacidad_pasajeros',
            field=models.CharField(help_text='Capacidad de Pasajeros de Vehículo', max_length=20),
        ),
        migrations.AlterField(
            model_name='flotavehicular',
            name='cilindraje',
            field=models.CharField(help_text='Cilindraje de Vehículo', max_length=20),
        ),
        migrations.AlterField(
            model_name='flotavehicular',
            name='kilometraje',
            field=models.CharField(help_text='Kilometraje de Vehículo', max_length=20),
        ),
    ]
