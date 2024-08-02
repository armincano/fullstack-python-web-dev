""" Título: Sistema de Puntuación Interactivo para un Juego de Niveles

Descripción:
Desarrolla un sistema de puntuación interactivo para un juego de niveles utilizando Python.
El sistema debe cumplir con los siguientes requisitos:

1. Utiliza un diccionario para almacenar los jugadores y sus puntuaciones.

2. Implementa una lista de niveles (Fácil, Medio, Difícil, Experto)
y sus correspondientes puntuaciones.

3. Recibe información de la consola para simular una ronda de juego:
   - Pide al usuario que ingrese el nombre del jugador actual.
   - Solicita el nivel completado por el jugador.
   - Pregunta por el tiempo que tardó en completar el nivel.

4. Valida la entrada del usuario:
   - Verifica que el jugador exista en el diccionario de jugadores.
   - Asegúrate de que el nivel ingresado sea válido.
   - Comprueba que el tiempo ingresado sea un número positivo.

5. Actualiza la puntuación del jugador basándote en el nivel completado.

6. Incluye un sistema de bonificación: 
si un jugador completa un nivel Difícil o Experto en 30 segundos o menos, 
recibe puntos extra.

7. Determina el líder actual del juego.
En caso de empate, muestra todos los jugadores empatados.

8. Muestra las puntuaciones actuales de todos los jugadores.

Restricciones:
- Utiliza estructuras if-else para la lógica condicional.
- Emplea operadores lógicos cuando sea necesario.
- Usa listas y diccionarios para almacenar y manipular datos.
- Utiliza input() para recibir información del usuario.

# Lista de niveles con sus respectivos puntos
niveles = ["Fácil", "Medio", "Difícil", "Experto"]
puntos_por_nivel = [10, 20, 30, 50]
"""

niveles = ["Fácil", "Medio", "Difícil", "Experto"]
puntos_por_nivel = [10, 20, 30, 50]

player_1= {"name": "Paulina", "score": 10}
player_2= {"name": "Juan", "score": 0}
player_3= {"name": "Chespirito", "score": 50}

print("¡Bienvenido al sistema de puntuación interactivo para un juego de niveles!")
print("Los jugadores actuales son: "+player_1["name"]+", "+player_2["name"]+" y "+player_3["name"])
   
player_name = input("Por favor, ingresa un nombre de jugador: ")
level = input("Por favor, ingresa el nivel completado (Fácil, Medio, Difícil, Experto): ")
time_to_complete = int(input("Por favor, ingresa el tiempo que tardaste en completar el nivel (en segundos): "))

if player_1["name"] == player_name or player_2["name"] == player_name or player_3["name"] == player_name:
    if level in niveles:
        if time_to_complete > 0:
            print("¡Información ingresada correctamente!")

            selected_player = {}
            if player_1["name"] == player_name: selected_player = player_1
            elif player_2["name"] == player_name: selected_player = player_2
            else: selected_player = player_3

            if level == "Fácil":
                if time_to_complete <= 30:
                   selected_player["score"] += puntos_por_nivel[0] + 5
                else:
                   selected_player["score"] += puntos_por_nivel[0]
            elif level == "Medio":
                if time_to_complete <= 30:
                     selected_player["score"] += puntos_por_nivel[1] + 5
                else:
                     selected_player["score"] += puntos_por_nivel
            elif level == "Difícil":
                if time_to_complete <= 30:
                     selected_player["score"] += puntos_por_nivel[2] + 5
                else:
                     selected_player["score"] += puntos_por_nivel[2]
            else:
                if time_to_complete <= 30:
                     selected_player["score"] += puntos_por_nivel[3] + 5
                else:
                     selected_player["score"] += puntos_por_nivel[3]
                     
            print("Puntuaciones actuales:")
            print(player_1["name"]+": "+str(player_1["score"]))
            print(player_2["name"]+": "+str(player_2["score"]))
            print(player_3["name"]+": "+str(player_3["score"]))
            
        else:
            print("Error: El tiempo ingresado debe ser un número positivo.")
    else:
        print("Error: El nivel ingresado no es válido.")
else: print("Error: El jugador ingresado no existe.")