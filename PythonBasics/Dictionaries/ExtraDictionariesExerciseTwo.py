# 2. Agrupar empleados por departamento
# Dada una lista de empleados donde cada uno tiene nombre, correo 
# y departamento, cree un diccionario que agrupe los empleados 
# por su departamento:
# Ejemplo:
#     Entrada:


employees = [
    {"name": "Carlos", "email": "carlos@empresa.com", "department": "Ventas"},
    {"name": "Ana", "email": "ana@empresa.com", "department": "IT"},
    {"name": "Luis", "email": "luis@empresa.com", "department": "Ventas"},
    {"name": "Sofía", "email": "sofia@empresa.com", "department": "RRHH"},
]

grouped_employees = {}

for employee in employees:
    if(employee["department"] in grouped_employees):
        grouped_employees[employee["department"]].append({"name":employee["name"], "email":employee["email"]})
    else:
        grouped_employees[employee["department"]]= [{"name":employee["name"], "email":employee["email"]}]


print("Grouped Employees Dictionary:")
print(grouped_employees)