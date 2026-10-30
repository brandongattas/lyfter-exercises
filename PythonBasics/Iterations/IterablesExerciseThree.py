# Cree un programa que intercambie el primer y ultimo elemento de una lista. Debe funcionar con listas de cualquier tamaño.
# Ejemplos:
# my_list = [4, 3, 6, 1, 7] → [7, 3, 6, 1, 4]

my_list = [4, 3, 6, 1, 7]
print(f"Initial List: {my_list}")

deleted_first_item = my_list.pop(0)
deleted_last_item = my_list.pop(len(my_list)-1)

my_list.insert(0, deleted_last_item)
my_list.insert(len(my_list), deleted_first_item)

print(f"Modified List: {my_list}")