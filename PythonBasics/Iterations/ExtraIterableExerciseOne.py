# 1. Cree un programa que cuente cuántas veces aparece un número específico en una lista. 
# Pida al usuario una lista de números y otro número a buscar
# Ejemplo:
#     Entrada:
#     my_list = [4, 2, 7, 2, 8, 2, 1]
#     numero_a_buscar = 2

#     Salida
#     "El número 2 aparece 3 veces"

list_size = int(input("Enter the size of the numbers list: "))
target_number = int(input("Enter the number that you wish to search in the list: "))
numbers_list = []
counter = 1
target_number_occurences_count = 0

print("---")
while(counter<=list_size):
    numbers_list.append(int(input(f"Enter the #{counter} number to store in the list: ")))
    counter+=1

for record in numbers_list:
    if(record==target_number):
        target_number_occurences_count+=1

print(f"The target number {target_number}, appears {target_number_occurences_count} times in the list.")