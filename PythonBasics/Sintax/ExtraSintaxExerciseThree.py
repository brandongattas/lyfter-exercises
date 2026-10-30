#Convertidor de unidades de temperatura
#Pida al usuario ingresar una temperatura en Celsius
#Conviértala a Fahrenheit y Kelvin
#Muestre los tres valores
#Ejemplo:
# Entrada:
#   "Ingrese temperatura en Celsius:" 25
# Salida:
#   Fahrenheit: 77.0
#   Kelvin: 298.15

celsius_temp = float(input("Input the temperature in celsius: "))
fahrenheit_temp = (celsius_temp*1.8)+32
kelvin_temp = celsius_temp+273.15

print (f"{celsius_temp} Celsius are {fahrenheit_temp} Fahrenheit.")
print (f"{celsius_temp} Celsius are {kelvin_temp} Kelvin.")