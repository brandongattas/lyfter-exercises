# Tabla de multiplicar personalizada
# Pida al usuario un número del 1 al 10
# Muestre su tabla de multiplicar del 1 al 12
# Ejemplo:
# Entrada:
#   "Ingrese un número:" 7
# Salida:
#   7 x 1 = 7
#   7 x 2 = 14
#   ...
#   7 x 12 = 84


while True:
    number = int(input("Enter a number between 1 and 10: "))

    if 1 <= number <= 10:
        print(f"Thank you! You entered a valid number: {number}")
        break
    else:
        print("Out of range. Please try again.")

counter = 1

while counter<=12:
    print(f"{number} x {counter} = {number*counter}")
    counter+=1