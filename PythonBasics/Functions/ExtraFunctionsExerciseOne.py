# 1. Cree una función que reciba un texto y un carácter, y retorne 
# cuántas veces aparece ese carácter en el texto
# Ejemplo:

#     Entrada:
#         "programacion"
#         "Ingrese el carácter que desea buscar:" "o"

#     Salida:
#         "Se ha encontrado 2 veces el carácter"

def count_char_in_string(my_string, searched_char):
    char_count=0

    for char in my_string:
        if char==searched_char:
            char_count+=1

    return char_count

my_string=input("Enter a string: ")
searched_char=""
while len(searched_char)!=1:
    searched_char=input("Enter the character that you want to search in the entered string: ")
    if len(searched_char)!=1:
        print("Error: You must enter exactly one character.")
print(f"Thank you, you entered: {searched_char}")

print(f"The script has found {count_char_in_string(my_string, searched_char)} times the character '{searched_char}' in the string '{my_string}'")