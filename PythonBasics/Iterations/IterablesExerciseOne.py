# Cree un programa que itere e imprima los valores de dos listas del mismo tamaño al mismo tiempo.
# Ejemplos:
# first_list = [’Hay’, ‘en’, ‘que’, ‘iteracion’, ‘indices’, ‘muy’]
# second_list = [’casos’, 'los’, ‘la’, ‘por’, ‘es’, ‘util’] ->
# Hay casos
# en los
# que la
# iteracion por
# indice es
# muy util

first_list = ["Hay", "en", "que", "iteracion", "indices", "muy"]
second_list = ["casos", "los", "la", "por", "es", "util"]

for index in range(0, len(first_list)):
    record_first_list = first_list[index]
    record_second_list = second_list[index]
    print(f"{record_first_list} {record_second_list}")

