# 1. Cree un programa que:
# Pida al usuario su nombre
#   Si el nombre es numérico (isdigit()), haga raise 
# ValueError("El nombre no puede ser un número")
# Ejemplo:
#       Entrada: "Ingrese su nombre: " 5
#       Salida:  "El nombre no puede ser un número"
#
# Luego pida su edad
# Si no es un número válido, capture el ValueError y muestre un mensaje
# Ejemplo:
# Entrada: "Ingrese su edad: " cinco
# Salida: "Número no valido"
#
# Si todo sale bien, imprima un mensaje: "Hola <nombre>, su edad es <edad>"
# Ejemplo:
# Entrada: "Ingrese su nombre: " "Jean Carlo"
# 		"Ingrese su edad: " 27
# Salida: Hola Jean Carlo, su edad es 27

def enter_name():
	name=""
	try:
		name=input("Enter your name: ")			
		if name.isdigit():
			raise ValueError
	except ValueError as ve:
		print("#### The name cannot be a number, please enter a valid name. ####")
		raise ve
	return name

def enter_age():
	age=""
	try:
		age=input("Enter your age: ")
		if not age.isdigit():
			raise ValueError
	except ValueError as ve:
		print("#### The number is invalid, please enter a valid age number. ####")
		raise ve
	return age


def main():
	try:
		print(f"Hi {enter_name()}, your age is {enter_age()}.")

	except Exception as ex:
		print(ex)

if __name__ == '__main__':
	main()