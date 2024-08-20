suma = 3000
contador = 0
try:
    if contador == 0:
        raise ZeroDivisionError("División por cero.")
    division = suma / contador
    print(division)
except ZeroDivisionError as e:
    print(e)