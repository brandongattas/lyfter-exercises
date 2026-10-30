# Cree un programa que itere e imprima un string letra por letra de derecha a izquierda.
# Pista: investigue de que otras maneras se puede usar el range.
# Ejemplos:
# my_string = ‘Pizza con piña’ →
# a
# ñ
# i
# p

# n
# o
# c

# a
# z
# z
# i
# p

my_string = input("Input a string: ")

for index in range(len(my_string)-1, -1, -1):
    print(my_string[index])

#Explicacion de range(len(my_string)-1, -1, -1)
#len(my_string)-1 = comenzara en ultimo index valido al disminuir 1 a my_string Ex. pizza len es 5-1= 4 seria el index.
#-1 de enmedio = significa que va a parar en index 1 -1 = 0, que es el index valido del string
#-1 de ultimo = significa que ira restando -1 en cada iteration