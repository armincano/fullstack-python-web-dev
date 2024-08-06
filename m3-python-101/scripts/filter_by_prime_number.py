students_list = [
    {'nombre': 'Juan', 'edad': 17, 'calificaciones': [85, 90, 88]},
    {'nombre': 'María', 'edad': 19, 'calificaciones': [92, 89, 90]},
    {'nombre': 'Pedro', 'edad': 21, 'calificaciones': [85, 95, 80]},
    {'nombre': 'Ana', 'edad': 18, 'calificaciones': [90, 92, 87]},
    {'nombre': 'Luis', 'edad': 20, 'calificaciones': [88, 85, 92]},
]
""" 
1. Imprimir los elementos que cumplan los siguientes filtros:
- edad mayor a 18
- promedio de calificaciones mayor a 85
2. Además, imprime el promedio de calificaciones de los estudiantes que cumplen
con los filtros anteriores y cuya edad es un número primo.
Número primo es aquel número entero mayor que 1 y con solo 2 divisores (1 and themselves) that don't leave a remainder.
"""
students_older_than_18_and_greater_85_grade = []

for student in students_list:
    is_older_than_18 = student['edad'] >= 18
    is_average_grade_greater_85 = sum(student['calificaciones']) / len(student['calificaciones']) > 85
    
    if is_older_than_18 and is_average_grade_greater_85:
        students_older_than_18_and_greater_85_grade.append(student)

filtered_students_with_prime_age = []

for student in students_older_than_18_and_greater_85_grade:
    is_prime = True
    for i in range(2, student['edad']):
        if student['edad'] % i == 0:
            is_prime = False
            break
    if is_prime:
        filtered_students_with_prime_age.append(student)

print("Estudiantes mayores de 18 años y con promedio de calificaciones mayor a 85:")
for student in students_older_than_18_and_greater_85_grade:
    formatted_student = f"Nombre: {student['nombre']}, Edad: {student['edad']}, Calificaciones: {student['calificaciones']}"
    print(formatted_student)

print("")
print("Promedio de calificaciones de estudiantes filtrados cuya edad es un número primo:")
for student in filtered_students_with_prime_age:
    average_grade = round(sum(student['calificaciones']) / len(student['calificaciones']))
    print(f"El promedio de calificaciones de {student['nombre']} es {average_grade}")