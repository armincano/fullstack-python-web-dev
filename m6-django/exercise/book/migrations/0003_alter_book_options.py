# Generated by Django 5.1.1 on 2024-10-22 01:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_alter_book_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': (('development', 'Can do development'), ('scrum_master', 'Can do scrum master'), ('product_owner', 'Can do product owner')), 'verbose_name': 'Libro', 'verbose_name_plural': 'Libros'},
        ),
    ]