# 3. Cree una función sumar_valores(lista) que:
# Reciba una lista de elementos (strings, enteros, flotantes mezclados)
# Intente convertir cada elemento a tipo float
# Si puede, sume el valor y muestre: "<valor> sumado correctamente"
# Si no puede, muestre: "Elemento inválido: <valor>"
# Al final, imprima la suma total
# Ejemplo:
#     Entrada:
#         my_list = ['10', 'manzana', '5.5', '3', 'n/a']
#     Salida:
#         10.0 "sumado correctamente"
#         "Elemento inválido: manzana"
#         5.5 "sumado correctamente"
#         3.0 "sumado correctamente"
#         "Elemento inválido: n/a"
#         "Total de la suma:" 18.5

def values_addition(list=[]):
	total_sum=0.0
	for value in list:
		try:
			total_sum+=float(value)
			print(f"{float(value)} added correctly.")
		except ValueError:
			print(f"Element is invalid: {value}")
			
	print(f"Total sum is: {total_sum}")


def main():
	try:
		mixed_list=[]
		counter=1
		qty_str_to_enter=int(input("Enter the values quantity that will be added to the list: "))
		while(counter<=qty_str_to_enter):
			mixed_list.append(input(f"Enter the value #{counter}: "))
			counter+=1

		print("")
		values_addition(mixed_list)

	except Exception as ex:
		print(ex)

if __name__ == '__main__':
	main()