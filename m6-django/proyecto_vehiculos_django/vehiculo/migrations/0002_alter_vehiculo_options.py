# Generated by Django 5.1.2 on 2024-10-23 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vehiculo',
            options={'permissions': [('can_see_catalog', 'Puede ver el catálogo de vehículos')]},
        ),
    ]
