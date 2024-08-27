# Generated by Django 5.0.7 on 2024-08-06 20:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Carro', '0002_brand_alter_car_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='value',
            field=models.FloatField(blank=True, null=True, verbose_name='Valor'),
        ),
        migrations.AlterField(
            model_name='brand',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='car',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='car_brand', to='Carro.brand', verbose_name='Marca'),
        ),
        migrations.AlterField(
            model_name='car',
            name='factory_year',
            field=models.IntegerField(blank=True, null=True, verbose_name='Ano de fabricação'),
        ),
        migrations.AlterField(
            model_name='car',
            name='model',
            field=models.CharField(max_length=200, verbose_name='Modelo'),
        ),
        migrations.AlterField(
            model_name='car',
            name='model_year',
            field=models.IntegerField(blank=True, null=True, verbose_name='Ano do modelo'),
        ),
    ]
