import random


random_number = random.randint(1, 10)

guessing_number = int(input("Guess a number between 1 and 10: "))

while guessing_number != random_number:
    guessing_number = int(input("Wrong number! - Guess again anumber between 1 and 10: "))


print("Congratulations! You guessed the number!")