# 2. Cree un programa que verifique si todos los elementos de una lista 
# son positivos
# Restricciones:
# No use funciones como all()
# Ejemplo:
# Entrada:
# my_list = [3, 6, 0, -2, 4]
# Salida:
# "Hay al menos un número negativo o cero"


list_size = int(input("Enter the size of the numbers list: "))
numbers_list = []
counter = 1
all_numbers_positive=True

print("---")
while(counter<=list_size):
    numbers_list.append(int(input(f"Enter the #{counter} number to store in the list: ")))
    counter+=1

for record in numbers_list:
    if(record==0 or record<0):
        print("There is at least one negative number or zero.")
        all_numbers_positive=False
        break

if all_numbers_positive and list_size>0:
    print("All the numbers in the list are positive/greater than zero.")
elif list_size<=0:
    print("The list of numbers is empty.")