""" 
1. eliminar todas las vocales de la palabra "paralelepípedo"
2. imprimir en pantalla las consonantes restantes y su posición dentro de dicha palabra """

word_1 = "paralelepípedo"
vowels = "aeiouáéíóú"
no_vocals_in_word = ""

for i in word_1.lower():
    if i not in vowels:
        no_vocals_in_word += i
        
print(no_vocals_in_word)

for i in range(len(no_vocals_in_word)):
    print(no_vocals_in_word[i], i)