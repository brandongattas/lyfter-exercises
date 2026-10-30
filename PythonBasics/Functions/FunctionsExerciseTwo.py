# Experimente con el concepto de scope:

# 1. Intente acceder a una variable definida dentro de una función 
# desde afuera.
def funtion_with_variable():
    my_string = "Hello world"

#print(my_string)  #variable does not exist globally, only inside the function.



# 2. Intente acceder a una variable global desde una función y 
# cambiar su valor.
my_global_counter=0

def add_numbers_to_counter():
    counter=1
    desired_numbers_qty = int(input("Cantidad de numeros desea sumar: "))

    while(counter<=desired_numbers_qty):
        global my_global_counter
        my_global_counter+=int(input(f"Ingrese el #{counter} numero que desea agregar al contador: "))
        counter+=1

add_numbers_to_counter()

print(f"Total global counter: {my_global_counter}")