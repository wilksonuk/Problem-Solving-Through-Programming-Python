# Need build a calculator.
def calculator():
    print("Calculator")
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ")

    if operation == "+":
        result = number1 + number2
    elif operation == "-":
        result = number1 - number2
    elif operation == "*":
        result = number1 * number2
    elif operation == "/":
        if number2 != 0:
            result = number1 / number2
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Error: Invalid operation."

    return f"The answer is: {result}"
print(calculator())