"""
1. Analice un número, e indique
- si es positivo o negativo
- si es par o impar
- En caso de ser cero, también indicarlo.

Restricciones
- Usar la expresión if-elif-else, y no usar subcondiciones;
en su lugar, usar condiciones anidadas. """

number = -2

if type(number) != int:
    print("Este programa sólo trabaja con números")
elif number > 0:
    if number % 2 == 0:
        print("El número es positivo y par")
    else:
        print("El número es positivo e impar")
elif number < 0:
    if number % 2 == 0:
        print("El número es negativo y par")
    else:
        print("El número es negativo e impar")
else: print("El número es cero")