# 3. Cree un programa que use una lista para eliminar keys de un diccionario.
# Ejemplos:
# list_of_keys = [’access_level’, ‘age’]
# employee = {’name’: ‘John’, ‘email’: ‘john@ecorp.com’, ‘access_level’: 5, ‘age’: 28}
# → {’name’: ‘John’, 'email’: ‘john@ecorp.com’}

list_of_keys = ["access_level", "age"]

employee = {"name": "John", "email": "john@ecorp.com", "access_level": 5, "age": 28}

print("")
print(f"Dictionary prior removing keys: {employee}")

for record in list_of_keys:
    employee.pop(record)

print("")
print(f"Dictionary with removed keys: {employee}")
