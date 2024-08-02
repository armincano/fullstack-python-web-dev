"""
1. Requerimos crear una variable con el número 8, una con el número 10.5,
y una con la palabra “ejercicio”.
2. Luego, crear un set que contendrá cada una de las variables que creamos,
y será asignado a una variable.
3. A continuación, crearemos una lista que contendrá el set creado anteriormente,
y una variable con el valor lógico False.
4. Esta lista la asignaremos a una variable que luego imprimiremos en pantalla. """

number_1 = 8
number_2 = 10.5
word_1 = "ejercicio"

word_set = {number_1, number_2, word_1}

exercise_list = [word_set, False]

print(exercise_list)