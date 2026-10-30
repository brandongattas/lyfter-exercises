# 5. Cree un programa que le pida al usuario ingresar 5 palabras. 
# Luego muestre una nueva lista con solo aquellas palabras que tengan más
# de 4 letras
# Ejemplo:
#     Entrada:
#         ['sol', 'estrella', 'luz', 'planeta', 'roca']
#     Salida:
#         ['estrella', 'planeta']


list_of_words = []
list_of_word_with_more_than_four_letters=[]
counter=1

while counter<=5:
    word = input(f"Enter your #{counter} word: ")
    list_of_words.append(word)
    counter+=1
    if(len(word)>4):
        list_of_word_with_more_than_four_letters.append(word)

print(f"Initial words list: {list_of_words}")
print(f"List of words that has more than 4 letters: {list_of_word_with_more_than_four_letters}")