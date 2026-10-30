# 3. Dada una lista de productos vendidos, donde cada uno 
# tiene categoría y precio, cree un diccionario que acumule 
# el total por categoría.
# Ejemplo:
# Entrada:


products = [
    {"name": "Monitor", "category": "Electrónica", "price": 200},
    {"name": "Teclado", "category": "Electrónica", "price": 50},
    {"name": "Silla", "category": "Muebles", "price": 120},
    {"name": "Mesa", "category": "Muebles", "price": 180},
    {"name": "Mouse", "category": "Electrónica", "price": 25},
]

total_per_category={}

for product in products:
    if(product["category"] in total_per_category):
        total_per_category[product["category"]]+=product["price"]
    else:
        total_per_category[product["category"]]=product["price"]

print(total_per_category)