from django.db import models

class Vehiculo(models.Model):
    MARCA_CHOICES = [
        ('FORD', 'Ford'),
        ('CHEVROLET', 'Chevrolet'),
        ('TOYOTA', 'Toyota'),
        ('FIAT', 'Fiat'),
    ]
    CATEGORIA_CHOICES = [
        ('PARTICULAR', 'Particular'),
        ('TRANSPORTE', 'Transporte'),
        ('CARGA', 'Carga'),
    ]
    marca = models.CharField(max_length=20, choices=MARCA_CHOICES, default='FORD')
    modelo = models.CharField(max_length=100)
    serial_carroceria = models.CharField(max_length=50)
    serial_motor = models.CharField(max_length=50)
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES, default='PARTICULAR')
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    
    class Meta:
        permissions = [
            ('can_see_catalog', 'Puede ver el catálogo de vehículos'),
        ]