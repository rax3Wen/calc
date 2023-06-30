import math

# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero!"

# Function to calculate the logarithm of a number
def logarithm(x):
    if x > 0:
        return math.log10(x)
    else:
        return "Error: Invalid input for logarithm!"

# Main program loop
while True:
    print("Select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Logarithm")
    print("6. Exit")

    choice = input("Enter the operation number: ")

    if choice == '6':
        print("Program terminated.")
        break

    if choice == '5':
        num = float(input("Enter a number: "))

        print("log(", num, ") =", logarithm(num))
        continue

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))
    elif choice == '2':
        print(num1, "-", num2, "=", subtract(num1, num2))
    elif choice == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))
    elif choice == '4':
        print(num1, "/", num2, "=", divide(num1, num2))
    else:
        print("Invalid input. Please try again.")