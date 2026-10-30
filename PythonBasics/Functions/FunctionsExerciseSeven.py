# Cree una función que acepte una lista de números y retorne una 
# lista con los números primos de la misma.

#    1. [1, 4, 6, 7, 13, 9, 67] → [7, 13, 67]

#    2. Tip 1: Investigue la lógica matemática para averiguar 
#       si un número es primo, y conviértala a código. No busque 
#       el código, eso no ayudaría.

#    3. Tip 2: Aquí hay que hacer varias cosas (recorrer la lista, 
#       revisar si cada numero es primo, y agregarlo a otra lista).
#       Así que lo mejor es agregar otra función para revisar si 
#       el numero es primo o no.

def get_prime_numbers_only(my_numbers_list=[]):
    prime_numbers_list=[]
    for index in range(len(my_numbers_list)):
        if is_prime(my_numbers_list[index]):
            prime_numbers_list.append(my_numbers_list[index])
    return prime_numbers_list

def is_prime(number):
    if number <= 1:  #numbers less than or equal are not prime
        return False
    
    if number == 2: #2 is the only even prime number
        return True
    
    if number % 2 == 0: #Exclude all other even numbers
        return False

    # Test only odd potential factors up to the square root of n
    for i in range(3, int(number**0.5) + 1, 2):
        if number % i == 0:
            return False
            
    return True


counter=1
numbers_qty=int(input("Ingrese la cantidad de numeros que tendra la lista: "))
list_of_numbers=[]

while counter<=numbers_qty:
    list_of_numbers.append(int(input(f"Ingrese el #{counter} number: ")))
    counter+=1

print(f"Original list of numbers: {list_of_numbers}")

print("--------------------")

print(f"List of prime numbers from original list: {get_prime_numbers_only(list_of_numbers)}")