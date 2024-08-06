""" Desafío: Adivina el Número Secreto
Objetivo: Implementar un juego en Python donde el usuario debe adivinar un número secreto entre 1 y 100. 
El programa debe indicar si el número ingresado es mayor o menor al número secreto
y continuar preguntando hasta que el usuario lo adivine.

Instrucciones:
1. Generar un número secreto aleatorio entre 1 y 100.
2. Pedir al usuario que adivine el número secreto.
3. Comparar el número ingresado por el usuario con el número secreto:
    - Si el número ingresado es mayor que el número secreto, mostrar el mensaje: "El número secreto es menor. Intenta de nuevo."
    - Si el número ingresado es menor que el número secreto, mostrar el mensaje: "El número secreto es mayor. Intenta de nuevo."
    - Si el número ingresado es igual al número secreto, mostrar el mensaje: "¡Felicidades! Has adivinado el número secreto." y terminar el juego.
Continuar pidiendo al usuario que adivine hasta que acierte el número secreto. """

import random
import time

divider = "^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^"
divider_2 = "=^..^=   =^..^=   =^..^=    =^..^=    =^..^=    =^..^=    =^..^="
is_game_over = False

print(divider)
print("Bienvenido al Juego de Adivinar el Número Secreto")
time.sleep(2)
print("Instrucciones: Adivina un número entre 1 y 100")
time.sleep(2)
print(f"Generando número secreto... {random.randint(1, 100)}")
time.sleep(0.5)
print(f"Generando número secreto... {random.randint(1, 100)}")
time.sleep(0.5)
print(f"Generando número secreto... {random.randint(1, 100)}")
time.sleep(0.5)

secret_number = random.randint(1, 100)
print(f"Número secreto generado. Es {secret_number} :P ¡Comencemos!")
print(divider)

while not is_game_over:
    input_number = int(input("Ingresa tu número: "))
    is_input_greater = input_number > secret_number
    is_input_lower = input_number < secret_number
    if is_input_greater:
        print("El número secreto es menor. Intenta de nuevo.")
    elif is_input_lower:
        print("El número secreto es mayor. Intenta de nuevo.")
    else:
        is_game_over = True
        time.sleep(0.5)
        print(divider_2)
        print("¡Felicidades!")
        time.sleep(0.5)
        print("Has adivinado el número secreto.")

