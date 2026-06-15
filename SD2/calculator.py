# Author: Maria Caro
# Class: Software Development - Programming Design Principles - 5N2927
# Description: Calculator program applying programming and design principles.
# The program has a menu that allows the user to add, subtract,
# multiply, and divide two numbers.
# Last edited: 2026-03-07


class Calculator:
    """
    Calculator class that performs basic math operations.

    This class shows a menu, gets two numbers from the user,
    and performs addition, subtraction, multiplication, and division.
    """

    def __init__(self):
        self.result = 0.0

    def show_menu(self):
        # Display the calculator menu
        print("\n --- Calculator Menu ---")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

    def get_numbers(self):
        # Ask for the first number until the input is valid
        while True:
            user_input = input("Enter first number: ")
            try:
                number1 = float(user_input)
                break
            except ValueError:
                print("Please enter a valid number.")

        # Ask for the second number until the input is valid
        while True:
            user_input = input("Enter second number: ")
            try:
                number2 = float(user_input)
                break
            except ValueError:
                print("Please enter a valid number.")

        return number1, number2

    def add_numbers(self, n1, n2):
        return n1 + n2

    def subtract_numbers(self, n1, n2):
        return n1 - n2

    def multiply_numbers(self, n1, n2):
        return n1 * n2

    def divide_numbers(self, n1, n2):
        # Prevent division by zero
        if n2 == 0.0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return n1 / n2


def main():
    # Create a single Calculator object to use throughout the program
    # This object will handle all calculator operations
    calculator = Calculator()

    # Keep running until the user chooses to exit
    while True:
        calculator.show_menu()
        choice = input("Select an option: ")

        if choice == "5":
            print("Calculator program ended.")
            break

        elif choice == "1":
            n1, n2 = calculator.get_numbers()
            result = calculator.add_numbers(n1, n2)
            print(f"The sum of {n1:.2f} and {n2:.2f} is {result:.2f}")

        elif choice == "2":
            n1, n2 = calculator.get_numbers()
            result = calculator.subtract_numbers(n1, n2)
            print(f"The difference between {n1:.2f} and {n2:.2f} is {result:.2f}")

        elif choice == "3":
            n1, n2 = calculator.get_numbers()
            result = calculator.multiply_numbers(n1, n2)
            print(f"The product of {n1:.2f} and {n2:.2f} is {result:.2f}")

        elif choice == "4":
            n1, n2 = calculator.get_numbers()
            try:
                result = calculator.divide_numbers(n1, n2)
                print(f"The division of {n1:.2f} and {n2:.2f} is {result:.2f}")
            except ZeroDivisionError as error:
                print(error)

        else:
            print("Incorrect option. Please try again.")


# Run the program
if __name__ == "__main__":
    main()