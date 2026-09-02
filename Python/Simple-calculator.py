num1 = float(input("Enter first Number: "))
op = input("Enter op(+ - * /): ")
num2 = float(input("Enter second Number: "))

if op == '+':
    result = num1 + num2

elif op == '-':
    result = num1 - num2

elif op == '*':
    result = num1 * num2

elif op == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Cannot divide by zero"

else:
    result = "Invalid operator"

print("Result:", result)