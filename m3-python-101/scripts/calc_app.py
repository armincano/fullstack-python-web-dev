"""
1. Crear una función
- que sume dos números,
- otra que reste dos números,
- otra que multiplique dos números,
- otra que divida dos números.
2. Adicionalmente, crear una función
que acepte dos números como parámetros
y regrese el resultado en forma de tupla
de su suma, resta, multiplicación y división.

Los resultados se deben almacenar en un diccionario,
cuyas claves serán: Suma, Resta, Multiplicación y División,
y los valores de cada clave serán los resultados obtenidos
con la función creada anteriormente.

The four basic arithmetic operations are: Addition, Subtraction
Multiplication, Division. Its are results Sum, Difference, Product, Quotient.
However, is recommended changing variable names to avoid using built-in names.
"""
def add(num_1, num_2):
    return num_1 + num_2


def subtract(num_1, num_2):
    return num_1 - num_2


def multiply(num_1, num_2):
    return num_1 * num_2


def divide(num_1, num_2):
    if num_2 == 0:
        raise ValueError("Cannot divide by zero")
    return num_1 / num_2


def calc_operations(num1, num2):
    addition = add(num1, num2)
    subtraction = subtract(num1, num2)
    multiplication = multiply(num1, num2)
    try:
        division = divide(num1, num2)
    except ValueError as e:
        print(f"Error: {e}")
        division = None
    results = (addition, subtraction, multiplication, division)
    return results


def calc_results_to_dict(*calc_results):
    if len(calc_results) != 4:
        return "A tuple with 4 values is required"
    elif calc_results[3] is None:
        return "Cannot divide by zero"
    
    operations_keys = ("addition", "subtraction", "multiplication", "division")
    results_dict = {}
    for count, value in enumerate(calc_results):
        results_dict.update({operations_keys[count]: value})
    return results_dict


results = calc_operations(4, 2)
results_dict = calc_results_to_dict(*results)
print(results_dict)