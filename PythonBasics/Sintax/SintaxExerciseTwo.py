name = input("Enter your name: ")
last_name = input("Enter your last name: ")
age = int(input("Enter your age: "))

if(age <= 2):
    print("You are a baby")
elif(age > 2 and age <= 9):
    print("You are a child")
elif(age > 9 and age <= 12):
    print("You are a pre-teen")
elif(age > 12 and age <= 17):
    print("You are a teenager")
elif(age > 17 and age <= 34):
    print("You are a young adult")
elif(age > 34 and age <= 59):
    print("You are an adult")
else:
    print("You are a senior")