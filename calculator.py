#!/usr/bin/env python3
"""
Simple Calculator
Supports basic arithmetic operations: addition, subtraction, multiplication, and division.
"""

def add(x, y):
    """Add two numbers"""
    return x + y

def subtract(x, y):
    """Subtract two numbers"""
    return x - y

def multiply(x, y):
    """Multiply two numbers"""
    return x * y

def divide(x, y):
    """Divide two numbers"""
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

def main():
    """Main calculator function"""
    print("=" * 40)
    print("Simple Calculator")
    print("=" * 40)
    print("\nOperations:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Exit")
    print("=" * 40)

    while True:
        try:
            choice = input("\nSelect operation (1-5): ").strip()

            if choice == '5':
                print("Thank you for using the calculator!")
                break

            if choice not in ['1', '2', '3', '4']:
                print("Invalid choice. Please select 1-5.")
                continue

            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                result = add(num1, num2)
                print(f"\n{num1} + {num2} = {result}")
            elif choice == '2':
                result = subtract(num1, num2)
                print(f"\n{num1} - {num2} = {result}")
            elif choice == '3':
                result = multiply(num1, num2)
                print(f"\n{num1} * {num2} = {result}")
            elif choice == '4':
                try:
                    result = divide(num1, num2)
                    print(f"\n{num1} / {num2} = {result}")
                except ValueError as e:
                    print(f"\nError: {e}")

        except ValueError:
            print("\nInvalid input. Please enter numeric values.")
        except KeyboardInterrupt:
            print("\n\nThank you for using the calculator!")
            break

if __name__ == "__main__":
    main()
