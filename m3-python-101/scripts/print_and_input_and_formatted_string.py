""" Desafío: Evaluación de Información Personal
Descripción:
Vas a crear un programa que obtiene información personal de tres personas desde la consola 
y realiza algunos cálculos utilizando esta información.

Requisitos:
- Usa la función input() para obtener el nombre, edad y altura de tres personas a través de la consola.

- Calcula el promedio de las edades.
- Calcula el promedio de las alturas.
- Calcula el total de caracteres en los nombres.

- Imprime el promedio de las edades y alturas.
- Imprime el total de caracteres en los nombres. """

print("¡Bienvenido al programa de evaluación de información personal!")
print("Por favor, ingresa la información solicitada para tres personas.")

print("Persona 1:")
name1 = input("Por favor, ingresa tu nombre: ")
age1 = int(input("Por favor, ingresa tu edad: "))
height1 = float(input("Por favor, ingresa tu altura en metros: "))

print("Persona 2:")
name2 = input("Por favor, ingresa tu nombre: ")
age2 = int(input("Por favor, ingresa tu edad: "))
height2 = float(input("Por favor, ingresa tu altura en metros: "))

print("Persona 3:")
name3 = input("Por favor, ingresa tu nombre: ")
age3 = int(input("Por favor, ingresa tu edad: "))
height3 = float(input("Por favor, ingresa tu altura en metros: "))

average_age = (age1 + age2 + age3) / 3
average_height = (height1 + height2 + height3) / 3
total_name_caracters = len(name1) + len(name2) + len(name3)

print("El promedio de las edades es: ", average_age)
print(f"El promedio de las alturas es: {average_height}")
print(f"El total de caracteres en los nombres es: {total_name_caracters}")