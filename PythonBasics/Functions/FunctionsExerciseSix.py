# Cree una función que acepte un string con palabras separadas por
#  un guion y retorne un string igual pero ordenado alfabéticamente.
# 1. Hay que convertirlo a lista, ordenarlo, y convertirlo 
# nuevamente a string.
# 2. “python-variable-funcion-computadora-monitor” → 
#    “computadora-funcion-monitor-python-variable”

def sort_string(my_string):
    string_to_list=my_string.split("-")
    sorted_list=sorted(string_to_list)
    return "-".join(sorted_list)

initial_string=input("Enter multiple word (-) separated string to be sorted: ")

print(f"The initial string is: {initial_string}")

print(f"The sorted string is: {sort_string(initial_string)}")