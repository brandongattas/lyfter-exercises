# Cree una calculadora por linea de comando. Esta debe de tener un 
# número actual, y un menú para decidir qué operación hacer con 
# otro número:
# 1. Suma
# 2. Resta
# 3. Multiplicación
# 4. División
# 5. Borrar resultado
# Al seleccionar una opción, el usuario debe ingresar el nuevo 
# número a sumar, restar, multiplicar, o dividir por el actual. El 
# resultado debe pasar a ser el nuevo numero actual.
# Debe de mostrar mensajes de error si el usuario selecciona una 
# opción invalida, o si ingresa un número invalido a la hora de 
# hacer la operación.

def addition(current, new_value):
    return current + new_value

def subtraction(current, new_value):
    return current-new_value

def multiply(current, new_value):
    return current*new_value

def divide(current, new_value):
    try:
        return current/new_value
    except ZeroDivisionError as ex:
        raise ex
    

def clear():
    return 0

def run_calculator():
    result=0
    available_calc_operations={'1':addition,'2':subtraction,'3':multiply,'4':divide,'5':clear,'6':'exit'}
    user_picked_option=''

        
    try:
        while user_picked_option!="6":
            print("")
            print(f"Current number is: {result}")
            print("Enter the operation number to perform from the following list: ")
            print("1 - Addition")
            print("2 - Subtraction")
            print("3 - Multiply")
            print("4 - Divide")
            print("5 - Clear")
            print("6 - Exit Calculator")
            user_picked_option=input("Enter option: ")
            try:
                if user_picked_option!="6" and user_picked_option in available_calc_operations:
                    if user_picked_option=='5':
                        result=clear()
                    else:
                        result=available_calc_operations[user_picked_option](result, float(input("Enter the number to sum to current number: ")))
                elif user_picked_option not in available_calc_operations:
                    raise ValueError()
            except ValueError:
                print("#### Option invalid, please pick a valid option from the list. ####")
            except ZeroDivisionError as zde:
                print("#### Cannot divide by Zero! ####")
                print(zde)

    except Exception as ex:
        raise ex


def main():
    try:
        run_calculator()

    except Exception as ex:
        print(ex)


if __name__ == '__main__':
    main()