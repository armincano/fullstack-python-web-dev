from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    fabricante = models.ForeignKey('Fabricante', on_delete=models.CASCADE, related_name='productos', null=True, blank=True)

    def __str__(self):
        return self.nombre

class Fabricante(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre