num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

greater_num = 0

if(num1 > num2):
    if(num1 > num3):
        greater_num = num1
    else:
        greater_num = num3
else:
    if(num2 > num3):
        greater_num = num2
    else:
        greater_num = num3

print("The greatest number is:", greater_num)