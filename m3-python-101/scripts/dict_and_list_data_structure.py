""" Requerimos crear un registro de datos personales de tres personas.
1. Los datos que se necesitan son: su nombre, apellido y teléfono.
Para ello, generaremos un diccionario para cada una de las personas con los datos mencionados,
2. y luego los almacenaremos dentro de una lista.
3. Finalmente, imprimiremos en pantalla la lista. """

person_1 = {"name": "Paulina", "last_name": "Vargas", "phone": 12345678}
person_2 = {"name": "Juan", "last_name": "Pérez", "phone": 87654321}
person_3 = {"name": "Chespirito", "last_name": "Gómez", "phone": 12348765}

users_list = [person_1, person_2, person_3]

print(users_list)