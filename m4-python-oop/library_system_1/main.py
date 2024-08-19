""" Desafío: Sistema de Biblioteca
Objetivo
Crea un sistema simple de gestión de libros en una biblioteca.
Este sistema debe incluir diferentes tipos de materiales (libros, revistas, y periódicos),
cada uno con sus características y comportamiento específicos
utilizando conceptos de programación orientada a objetos como clases, herencia, atributos, propiedades y métodos.

Estructura del Desafío
1.  Clase Base - MaterialBiblioteca
1.1 Atributos de Instancia:
- titulo: El título del material (ej., "El Hobbit").
- autor: El autor del material (ej., "J.R.R. Tolkien").
- año_publicacion: El año en que el material fue publicado (ej., 1937).
1.2 Propiedad año_publicacion:
- Utiliza un método getter para obtener el año de publicación.
- Utiliza un método setter para asegurar que el año de publicación no sea un valor futuro.
Si se intenta establecer un año en el futuro, se lanza una excepción ValueError.
1.3 Método informacion:
- Devuelve una cadena con la información básica del material: título, autor y año de publicación.

2.  Clase Derivada - Libro
2.1 Hereda de MaterialBiblioteca.
2.2 Atributos Adicionales:
- numero_paginas: El número de páginas del libro (ej., 310).
2.3 Método informacion:
- Sobreescribe el método de la clase base para incluir también el número de páginas en la descripción del libro.

3.  Clase Derivada - Revista
3.1 Hereda de MaterialBiblioteca.
3.2 Atributos Adicionales:
- numero_edicion: El número de edición de la revista (ej., 800).
3.3 Método informacion:
- Sobreescribe el método de la clase base para incluir también el número de edición en la descripción de la revista.

4.  Clase Derivada - Periodico
4.1 Hereda de MaterialBiblioteca.
4.2 Atributos Adicionales:
- fecha: La fecha específica de la publicación del periódico (ej., "15-08-2024").
4.3 Método informacion:
- Sobreescribe el método de la clase base para incluir también la fecha de publicación en la descripción del periódico.

5.  Instanciación y Uso
5.1 Crea instancias de las clases Libro, Revista, y Periodico con datos de ejemplo.
5.2 Ajusta y accede a los atributos utilizando propiedades.
5.3 Imprime la información de cada material utilizando el método informacion.

Ejemplo de Funcionamiento
1.  Definición de Clases:
- Se definen las clases base y derivadas, cada una con sus atributos y métodos específicos.
2.  Método main:
- Se crean objetos de las clases Libro, Revista, y Periodico.
- Se imprime la información de cada objeto, demostrando el uso de herencia y métodos sobreescritos.
3.  Salida Esperada:
- La salida muestra la información completa de cada material, incluyendo los atributos adicionales específicos de cada tipo de material.
Este desafío te ayudará a comprender cómo utilizar la herencia y las propiedades en Python, además de cómo extender el comportamiento de una clase base en clases derivadas.

Título: El Hobbit, Autor: J.R.R. Tolkien, Año de Publicación: 1937, Número de Páginas: 310
Título: National Geographic, Autor: Varios, Año de Publicación: 2023, Número de Edición: 800
Título: El País, Autor: Varios, Año de Publicación: 2024, Fecha: 15-08-2024 """

from library_resources import Book, Magazine, Newspaper

def main():
    book_1=Book("El Hobbit", "J.R.R. Tolkien", 1937, 310)
    print(book_1.info())
    
    magazine_1=Magazine("National Geographic", "Varios", 2023, 800)
    print(magazine_1.info())
    
    newspaper_1=Newspaper("El País", "Varios", 2024, "15-08-2024")
    print(newspaper_1.info())
    
    book_1.publication_year=2025
    book_1.publication_year=2024
    print(book_1.info())
    
if __name__ == "__main__":
    main()