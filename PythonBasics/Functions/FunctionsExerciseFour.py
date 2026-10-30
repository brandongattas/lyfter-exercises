# Cree una función que le dé la vuelta a un string y lo retorne.
# Esto ya lo hicimos en iterables.
# “Hola mundo” → “odnum aloH”

def return_str_backwards(my_string):
    reversed_string = ""
    for index in range(len(my_string)-1, -1, -1):
        reversed_string+=my_string[index]
    return reversed_string


string_to_reverse=input("Ingrese el string que desea voltear: ")

print(f"Original String: {string_to_reverse} --> Reversed String: {return_str_backwards(string_to_reverse)}")