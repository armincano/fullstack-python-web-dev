# Generated by Django 5.1.3 on 2024-11-11 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserva_mesa', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserva',
            name='ocupada',
        ),
        migrations.AddField(
            model_name='cliente',
            name='rut',
            field=models.CharField(default='11111111-1', max_length=10, unique=True),
        ),
        migrations.AddField(
            model_name='mesa',
            name='ocupada',
            field=models.BooleanField(default=False),
        ),
    ]
