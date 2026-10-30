# 2. Cree una función convertir_a_entero(lista) que:
# Reciba una lista de strings
# Intente convertir cada elemento a entero usando int()
# Use try-except para atrapar los errores ValueError
# Si algún elemento no puede convertirse, mostrar "No se pudo convertir el elemento: <valor>" y continuar con los demás
# Ejemplo:
#     Entrada:
#         my_list = ['4', 'hola', '10', '5.2']
    
# Salida:
#     "Resultado:"
#     "4" "convertido a" 4
#     "No se pudo convertir el elemento: hola"
#     "10" "convertido a" 10
#     "No se pudo convertir el elemento: 5.2"

def convert_to_integer(str_list=[]):
	for str in str_list:
		try:
			print(f"'{str}' converted  to {int(str)}")
		except ValueError:
			print(f"Element was not able to be converted: {str}")

def main():
	try:
		str_list=[]
		counter=1
		qty_str_to_enter=int(input("Enter the string quantity that will be added to the list: "))
		while(counter<=qty_str_to_enter):
			str_list.append(input(f"Enter the word #{counter}: "))
			counter+=1

		print("")
		convert_to_integer(str_list)

	except Exception as ex:
		print(ex)

if __name__ == '__main__':
	main()