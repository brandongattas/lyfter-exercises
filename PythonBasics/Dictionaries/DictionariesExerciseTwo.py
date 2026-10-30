# 2. Cree un programa que cree un diccionario usando dos listas del mismo tamaño, usando una para sus keys, y la otra para sus values.
# Ejemplos:
# list_a = [’first_name’, ‘last_name’, ‘role’]
# list_b = [’Alek’, ‘Castillo’, ‘Software Engineer’]
# → {’first_name’: ‘Alek’, ‘last_name’: ‘Castillo’, ‘role’: ‘Software Engineer’}


list_a = ["first_name", "last_name", "role"]
list_b = ["Brandon", "Gattas", "Developer"]
dictionary = {}

for index in range(len(list_a)):
    dictionary[list_a[index]]=list_b[index]

print(f"Created dictionary: {dictionary}")