# 3. Cree una función que reciba un string y retorne cuántas vocales 
# contiene
# Ejemplo:
#     Entrada:
#         "Hola mundo"

#     Salida:
#         4


def vowels_counter(my_string):
    vowel_count=0
    vowels_list=['a','e','i','o','u','A','E','I','O','U']
    for char in my_string:
        if char in vowels_list:
            vowel_count+=1
    return vowel_count

my_string = input("Enter a string: ")

print(f"There are {vowels_counter(my_string)} vowels in the entered string: {my_string}")