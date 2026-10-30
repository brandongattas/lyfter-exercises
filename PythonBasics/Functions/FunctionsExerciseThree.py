# Cree una función que retorne la suma de todos los números de una
# lista.
# La función va a tener un parámetro (la lista) y retornar un 
# número (la suma de todos sus elementos).
# [4, 6, 2, 29] → 41

def sum_numbers_in_list(numbers=[]):
    sum=0
    for num in numbers:
        sum+=num
    return sum

list_of_numbers=[]
qty_numbers=int(input(f"Ingrese la cantidad de numeros que desea en la lista:"))
counter=1

print("-----------")

while counter<=qty_numbers:
    list_of_numbers.append(int(input(f"Ingrese el #{counter} numero para agregar a la lista: ")))
    counter+=1

print("-----------")
print(f"El total de todos los numeros en la lista es: {sum_numbers_in_list(list_of_numbers)}")