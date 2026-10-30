# Cree un programa que le pida un numero al usuario, y realice una suma de cada numero del 1 hasta ese número ingresado. 
# Luego muestre el resultado de la suma.
#  5 → 15 (1 + 2 + 3 + 4 + 5)
#  3 → 6 (1 + 2 + 3)
#  12 → 78 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12)

number = int(input("Provide the number: "))
sum = 0
counter = 0

while counter <= number:
    sum+=counter
    counter+=1

print(f"Total sum from 1 to {number} is: {sum}")