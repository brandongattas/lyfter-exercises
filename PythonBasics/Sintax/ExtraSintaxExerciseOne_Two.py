# Cree un programa que le pida un tiempo en segundos al usuario y calcule si es menor o mayor a 10 minutos. Si es menor, 
# muestre cuantos segundos faltarían para llegar a 10 minutos. Si es mayor, muestre “Mayor”. 
# Si es exactamente igual, muestre “Igual”.
# Ejemplos:
#   1040 → Mayor
#   140 → 460
#   600 → Igual
#   599 → 1


time_in_seconds = int(input("Provide the time in seconds format: "))
missing_seconds = 0

if time_in_seconds<600:
   missing_seconds=600-time_in_seconds
   print(f"Seconds remaining to complete 10 minutes: {missing_seconds}")
elif time_in_seconds>600:
   print("Mayor")
else:
   print("Igual")