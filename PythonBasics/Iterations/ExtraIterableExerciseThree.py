# 3. Cree un programa que muestre el valor más pequeño de una lista sin usar min().
# Use una variable para comparar uno a uno
# Ejemplo:
#     Entrada:
#     my_list = [9, 4, 7, 1, 5]

#     Salida:
#     "El menor valor es 1"

list_size = int(input("Enter the size of the numbers list: "))
numbers_list = []
counter = 1
smallest_number=0

print("---")
while counter<=list_size:
    number = int(input(f"Enter the #{counter} number to store in the list: "))
    numbers_list.append(number)
    
    if counter==1:
        smallest_number=number

    counter+=1
    if(number<smallest_number):
        smallest_number=number

print(f"The list of number entered is: {numbers_list}, and the smallest number entered is {smallest_number}")
