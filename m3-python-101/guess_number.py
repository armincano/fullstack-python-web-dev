""" Objetivo: Crear un programa que permita al usuario adivinar un número aleatorio entre 1 y 10 inclusivos. 
El programa debe dar una sola oportunidad al usuario para adivinar 
y debe indicar si el usuario adivinó correctamente o no.

Instrucciones:
1. Genera un número aleatorio entre 1 y 10 inclusivos y asígnalo a una variable.
2. Pide al usuario que ingrese el número que cree fue asignado.
3. Usa estructuras if y else para comparar el número del usuario con el número aleatorio.
4. Imprime un mensaje que indica al usuario si su adivinanza es correcta o no. """

import random
import time

divider = "^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^"

print(divider)
print("¡Bienvenido al juego de adivinar el número!")
print("Tienes una oportunidad para adivinar el número aleatorio entre 1 y 10.")
time.sleep(5)
print("¡Buena suerte!")
time.sleep(2)
print("Generando un número aleatorio...")
time.sleep(0.5)
print(random.randint(1, 10))
time.sleep(0.5)
print(random.randint(1, 10))
time.sleep(0.5)
print(random.randint(1, 10))
time.sleep(0.5)
random_number = random.randint(1, 10)
print("Número generado.")

print(divider)

user_guess_number = int(input("Adivina el número aleatorio entre 1 y 10, ingrésalo: "))
print("Procesando respuesta...")
time.sleep(1)
print("¿Le achuntaste? :O")
time.sleep(2)

print(divider)

if user_guess_number == random_number:
    print("¡Felicidades! Adivinaste el número.")
else: print("Lo siento, no adivinaste el número. El número era:", random_number)