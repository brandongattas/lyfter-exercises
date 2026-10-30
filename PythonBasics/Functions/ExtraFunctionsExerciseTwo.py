# 2. Cree una función que reciba una lista de palabras y un número
# n, y retorne una nueva lista con solo las palabras que tengan 
# más de n letras
# Ejemplo:
#
#     Entrada:
#         ["cielo", "sol", "maravilloso", "día"]
#         "Ingrese el numero de letras minimas en la palabra: " 4
#
#     Salida:
#         ["cielo", "maravilloso"]


def get_strings_with_minimum_letters(strings_list=[], letters_qty=0):
    new_string_list=[]
    for string in strings_list:
        if len(string)>letters_qty:
            new_string_list.append(string)
    return new_string_list

strings_list=[]
strings_qty = int(input("Enter the quantity of words that you want in the list: "))
minimum_letters_qty=int(input("Enter the minimum quantity of letters in each string: "))
counter=1

while counter<=strings_qty:
    strings_list.append(input(f"Enter #{counter} word: "))
    counter+=1

print(f"Entered list of words: {strings_list}")

print(f"The list with words that has more than {minimum_letters_qty} letters in their words is: {get_strings_with_minimum_letters(strings_list, minimum_letters_qty)}")