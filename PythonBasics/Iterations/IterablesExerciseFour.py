# Cree un programa que elimine todos los números impares de una lista.
# Ejemplos:
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9] → [2, 4, 6, 8]

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_without_odd_numbers = []
print(f"Initial list: {my_list}")

for index in range(0, len(my_list)):
    record = my_list[index]
    if(record%2 == 0):
        list_without_odd_numbers.append(record)

print(f"List with removed odd numbers: {list_without_odd_numbers}")