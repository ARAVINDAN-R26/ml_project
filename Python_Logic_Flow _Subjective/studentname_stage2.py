#Stage 2: Add Result Check

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /): ")
Result = 0

if operator == '+':
    Result = num1 + num2
elif operator == '-':
    Result = num1 - num2
elif operator == '*':
    Result = num1 * num2
elif operator == '/':
    if num2 == 0:
        print("Error: Division not possible")
    else:
        Result =  num1 / num2

if Result > 0:
    print("Positive")
elif Result < 0:
    print("Negative")
else:
    print("Zero")