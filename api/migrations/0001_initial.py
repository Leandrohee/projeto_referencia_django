# Generated by Django 5.0.3 on 2024-03-15 23:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pedido', models.IntegerField(validators=[django.core.validators.MaxValueValidator(9999)])),
                ('oficina', models.CharField(choices=[('Gas', 'Gasolina'), ('Dis', 'Diesel'), ('Pos', 'Posto'), ('Ele', 'Eletrica')], default='Gas', max_length=3)),
                ('os', models.CharField(max_length=10)),
                ('prefixo', models.CharField(max_length=10)),
                ('modelo', models.CharField(max_length=10)),
            ],
        ),
    ]