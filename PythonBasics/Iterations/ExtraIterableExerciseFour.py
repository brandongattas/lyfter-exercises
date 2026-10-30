# 4. Cree un programa que reciba una lista de números y calcule el promedio de los valores, luego cree una nueva lista con solo los valores mayores al promedio
# Ejemplo
#     Entrada
#         my_list = [10, 20, 30, 40, 50]
#     Salida:
#         "Promedio:" 30
#         Nueva lista: [40, 50]

list_size = int(input("Enter the size of the numbers list: "))
numbers_list = []
counter = 1
avg_list_number=0
sum_of_list_numbers=0
num_greater_than_avg_list=[]

print("---")
while counter<=list_size:
    number = int(input(f"Enter the #{counter} number to store in the list: "))
    numbers_list.append(number)
    counter+=1
    sum_of_list_numbers+=number

avg_list_number=sum_of_list_numbers//list_size

for record in numbers_list:
    if(record>avg_list_number):
        num_greater_than_avg_list.append(record)

print(f"Initial list of numbers: {numbers_list}")
print(f"The Average is: {avg_list_number}")
print(f"The list of numbers greater than the average is: {num_greater_than_avg_list}")