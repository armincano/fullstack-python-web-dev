from django.db import models

class MenuItem(models.Model):
    class Category(models.TextChoices):
        BEBIDA_CALIENTE = 'BEBIDA_CALIENTE', 'Bebida Caliente'
        BEBIDA_FRIA = 'BEBIDA_FRIA', 'Bebida Fría'
        POSTRE = 'POSTRE', 'Postre'
        SNACK = 'SNACK', 'Snack'
        SANDWICH = 'SANDWICH', 'Sandwich'
        
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(
        max_length=50,
        choices=Category.choices,
        default=Category.BEBIDA_CALIENTE
    )
    image = models.ImageField(upload_to='images/')