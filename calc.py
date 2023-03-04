import math

def calculator():
    print("Welcome to the scientific calculator, By FATAO!")
    while True:
        print("\nSelect an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Unit Conversion")
        print("6. Exit")

        choice = int(input("Enter choice (1-6): "))

        if choice == 1:
            add()

        elif choice == 2:
            subtract()

        elif choice == 3:
            multiply()

        elif choice == 4:
            divide()

        elif choice == 5:
            convert_units()

        elif choice == 6:
            print("Thank you for using the calculator!")
            break

        else:
            print("Invalid input. Please select a valid option.")


def add():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 + num2
    print("Result: ", result)


def subtract():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 - num2
    print("Result: ", result)


def multiply():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 * num2
    print("Result: ", result)


def divide():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 / num2
    print("Result: ", result)


def convert_units():
    print("\nSelect a conversion:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Kilometers to Miles")
    print("4. Miles to Kilometers")

    choice = int(input("Enter choice (1-4): "))

    if choice == 1:
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 1.8) + 32
        print("Temperature in Fahrenheit: ", fahrenheit)

    elif choice == 2:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) / 1.8
        print("Temperature in Celsius: ", celsius)

    elif choice == 3:
        kilometers = float(input("Enter distance in kilometers: "))
        miles = kilometers * 0.621371
        print("Distance in miles: ", miles)

    elif choice == 4:
        miles = float(input("Enter distance in miles: "))
        kilometers = miles / 0.621371
        print("Distance in kilometers: ", kilometers)

    else:
        print("Invalid input. Please select a valid option.")


calculator()
