# Step 1: Get input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose an operation (+, -, *, /): ")

# Step 2: Match case to decide
match operation:
    case "+":
        print(f"The result of {num1} + {num2} is {num1 + num2}")
    case "-":
        print(f"The result of {num1} - {num2} is {num1 - num2}")
    case "*":
        print(f"The result of {num1} * {num2} is {num1 * num2}")
    case "/":
        if num2 != 0:
            print(f"The result of {num1} / {num2} is {num1 / num2}")
        else:
            print("Error: Division by zero is not allowed.")
    case _:
        print("Invalid operation! Please choose +, -, * or /.")

