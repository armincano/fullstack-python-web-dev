class Figuras:
    def __init__(self, perimetro_lado:float, cantidad_lados:int):
        self._perimetro_lado = perimetro_lado
        self._cantidad_lados = cantidad_lados
        
    @property
    def perimetro_lado(self):
        return self._perimetro_lado
        
    @property
    def cantidad_lados(self):
        return self._cantidad_lados
        
    def calcular_perimetro(self):
        return self.perimetro_lado * self.cantidad_lados
    
figura_1 = Figuras(3,3)
print(figura_1.calcular_perimetro())

class Cuadrado(Figuras):
    def __init__(self, perimetro_lado:float):
        super().__init__(perimetro_lado, 4)

class Pentagono(Figuras):
    def __init__(self, perimetro_lado:float):
        super().__init__(perimetro_lado, 5)


class Exagono:
    pass


class Octagono:
    pass

cuadrado_1 = Cuadrado(3)
print(cuadrado_1.calcular_perimetro())

pentagono_1 = Pentagono(3)
print(pentagono_1.calcular_perimetro())
