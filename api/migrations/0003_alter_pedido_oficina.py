# Generated by Django 5.0.3 on 2024-03-16 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_pedido_modelo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='oficina',
            field=models.CharField(choices=[('Gasolina', 'GASOLINA'), ('Diesel', 'DIESEL'), ('Posto', 'POSTO'), ('Eletrica', 'ELETRICA')], default='Gas', max_length=15),
        ),
    ]
