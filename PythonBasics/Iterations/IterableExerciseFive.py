# Cree un programa que le pida al usuario 10 números, y al final le muestre todos los números que ingresó, 
# seguido del numero ingresado más alto.

# Ejemplos:
# 86, 54, 23, 54, 67, 21, 2, 65, 10, 32 → [86, 54, 23, 54, 67, 21, 2, 65, 10, 32]. El más alto fue 86.

greatest_number = 0
counter = 1
list_of_numbers = []

while(counter<=10):
    number = int(input(f"Enter the #{counter} number: "))
    list_of_numbers.append(number)
    if(number > greatest_number):
        greatest_number=number
    counter+=1

print(f"The list of entered numbers is: {list_of_numbers}, and the greatest number is {greatest_number}.")
