# Cree una función que imprima el número de mayúsculas y el número 
# de minúsculas en un string.
# “I love Nación Sushi” → “There’s 3 upper cases and 13 lower cases”

def print_upper_and_lower_case_letters_qty(my_string):
    lower_case_counter=0
    upper_case_counter=0

    for char in my_string:
        if char.isupper():
            upper_case_counter+=1
        elif char.islower():
            lower_case_counter+=1

    print(f"There are {upper_case_counter} upper cases and {lower_case_counter} lower cases")


print_upper_and_lower_case_letters_qty(input(f"Ingrese el string que desea scanear: "))