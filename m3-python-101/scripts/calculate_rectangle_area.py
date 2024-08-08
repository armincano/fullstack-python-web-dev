"""
Crear una función que acepte dos parámetros (base y altura)
y calcule el área de un rectángulo.
Validar que ambos sean números positivos."""

def calculate_rectangle_area(base, height):
    if base <= 0 or height <= 0:
        return "Ambos valores deben ser positivos"
    return base * height

print(calculate_rectangle_area(5, 10))
print(calculate_rectangle_area(0, 10))