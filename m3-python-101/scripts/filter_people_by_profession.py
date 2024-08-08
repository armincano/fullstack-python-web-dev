"""
1. Separar los nombres en tres grupos:
    -magos: Harry Houdini, David Blaine, Teller
    -científicos: Newton, Hawking, Einstein
    -otros: Messi, Pele, Juanes
2. Definir hacer_grandioso(), que modifica la lista de magos añadiendo la
frase 'El gran' antes del nombre de cada mago.
3. Definir imprimir_nombres(), que imprime el nombre de cada persona de la lista.
4. imprimir en pantalla la lista completa de nombres antes de ser modificados
5. imprimir los nombres de los magos grandiosos, los nombres de los científicos, y los restantes.
"""

famous_people_by_profession = {
    "magicians": ["Harry Houdini", "David Blaine", "Teller"],
    "scientists": ["Newton", "Hawking", "Einstein"],
    "misc": ["Messi", "Pele", "Juanes"],
}

def make_wonderful(dict):
    magician_prefix = "The Big "
    wonderful_dict=dict.copy()
    for key, names_list in wonderful_dict.items():
        if key=="magicians":
            for idx, magician in enumerate(names_list):
                wonderful_dict["magicians"][idx] = magician_prefix+magician
        break
    return wonderful_dict

def print_famous_people_names(dict, description_text):
    divider = "^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^"
    print(divider)
    print(description_text)
    for value in dict.values():
        for names in value:
            print(names)
            
print_famous_people_names(famous_people_by_profession, "Famous people names with no modifications:")
print_famous_people_names(make_wonderful(famous_people_by_profession), "Famous people names with modifications:")