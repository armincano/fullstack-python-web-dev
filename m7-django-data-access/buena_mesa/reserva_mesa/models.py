from django.db import models

class Cliente(models.Model):
    rut = models.CharField(max_length=10, unique=True, default='11111111-1')
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()
    direccion = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'
    
class Mesa(models.Model):
    numero = models.IntegerField()
    capacidad = models.IntegerField()
    ocupada = models.BooleanField(default=False)

    def __str__(self):
        return f'Mesa {self.numero}'
    
class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    creado_en = models.DateTimeField(auto_now_add=True)
    cantidad_personas = models.IntegerField()

    def __str__(self):
        return f'Reserva de {self.cliente} para {self.cantidad_personas} personas'
