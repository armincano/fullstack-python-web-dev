"""
1. Eliminar los elementos duplicados.
2. Ordenar la lista resultante en orden ascendente.

a prototype of what a set data structure does,
specifically in terms of removing duplicate elements from a list.
The code iterates through the list and removes any duplicate elements it encounters. 
"""

list_1 = [5, 20, 15, 20, 25, 50, 20, 5, 18, 15]

for i in range(len(list_1)):
    for j in range(i+1, len(list_1)):
        if len(list_1) <= j: # checking if the length of list_1 is less than or equal to the value of j. If it is, it means that list_1 is out of range at index j.
            break
        if list_1[j] == list_1[i]:
            list_1.pop(j)
    if len(list_1) <= i:
        break
            
sorted_list_1 = sorted(list_1)
print(sorted_list_1)
