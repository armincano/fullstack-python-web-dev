""" 
1. Imprimir cada dato con las siguientes excepciones:
- Si el primer número de la sublista es cero, omitir la impresión de toda la sublista,
- Si existe un cero en cualquier otra posición, omitir solo la impresión del cero.
2. Crear un diccionario donde asignaremos la primera sublista a la clave A, la
segunda a la clave B, la tercera a la clave C, y la cuarta a la clave D.
3. Imprimir el diccionario resultante.
"""

list_1 = [[1,2,3], [0,4,5], [4,0,1], [6,5,4]]

# Print each sublist with the following exceptions:
for sublist in list_1:
    sublist_to_print = []
    if sublist[0] == 0:
        continue
    for i in sublist:
        if i == 0:
            continue
        sublist_to_print.append(i)
    print(sublist_to_print)
    
ascii_code_upper_a = 65
dict_keys = []
for i in range(len(list_1)):
    dict_keys.append(chr(ascii_code_upper_a + i))
    
sublist_dict = {}
for count, letter in enumerate(dict_keys):
    new_sublist = {letter: list_1[count]}
    sublist_dict.update(new_sublist)

print(sublist_dict)
    
    

