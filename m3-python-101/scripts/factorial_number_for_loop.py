""" calcular el factorial de un número, asignarlo a una variable, y luego imprimirla
- factorial es el resultado de la multiplicación de todos los enteros positivos que hay
entre un número y uno"""
number_to_factorial = 3
factorial_result = 1

for i in range(1,number_to_factorial+1):
    factorial_result = factorial_result * i
    
print(factorial_result)