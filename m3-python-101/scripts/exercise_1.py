""" 
Crear una lista con 10 números enteros, recorrerla haciendo uso de la sentencia for,
e imprimir en pantalla el valor de cada elemento indicando si es par, impar o cero.
"""

ten_integers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for n in ten_integers:
    if n == 0:
        print(f"{n} es cero")
    elif n % 2 == 0:
        print(f"{n} es par")
    else:
        print(f"{n} es impar")
