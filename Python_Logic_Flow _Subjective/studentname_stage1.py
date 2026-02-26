#Stage 1: Basic Calculator

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /): ")

if operator == '+':
    print("Result = ", num1 + num2)
elif operator == '-':
    print("Result = ", num1 - num2)
elif operator == '*':
    print("Result = ", num1 * num2)
elif operator == '/':
    if num2 == 0:
        print("Error: Division not possible")
    else:
        print("Result = ", num1 / num2)