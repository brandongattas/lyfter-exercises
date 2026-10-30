# Cree un programa que pida 3 números al usuario. Si uno de esos números es 30, o si los 3 sumados dan 30, 
# mostrar “Correcto”. Sino, mostrar “incorrecto”.
# Ejemplos:
#  23, 30, 768 → Correcto (hay un 30)
#  10, 15, 5 → Correcto (10 + 15 + 5 = 30)
#  35, 56, 2 → Incorrecto (no hay ningún 30, y la suma de ellos tampoco da 30)


num1 = int(input("Input the first number: "))
num2 = int(input("Input the second number: "))
num3 = int(input("Input the third number: "))

sum = num1+num2+num3

if num1==30 or num2==30 or num3==30 or sum==30:
    print("Correcto")
else:
    print("Incorrecto")