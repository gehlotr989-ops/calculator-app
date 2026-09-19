import sys

class Calculator:
    def __init__(self):
        self.history = []

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b

    def show_history(self):
        if not self.history:
            print("\nNo history available.")
        else:
            print("\n--- Calculation History ---")
            for idx, entry in enumerate(self.history, 1):
                print(f"{idx}. {entry}")

    def run(self):
        print("=== Feature-Rich CLI Calculator ===")
        while True:
            print("\nSelect Operation:")
            print("1. Add (+)")
            print("2. Subtract (-)")
            print("3. Multiply (*)")
            print("4. Divide (/)")
            print("5. View History")
            print("6. Exit")

            choice = input("Enter choice (1-6): ").strip()

            if choice == '6':
                print("Exiting calculator. Goodbye!")
                break
            elif choice == '5':
                self.show_history()
                continue
            elif choice in ('1', '2', '3', '4'):
                try:
                    num1 = float(input("Enter first number: "))
                    num2 = float(input("Enter second number: "))

                    if choice == '1':
                        result = self.add(num1, num2)
                        op = '+'
                    elif choice == '2':
                        result = self.subtract(num1, num2)
                        op = '-'
                    elif choice == '3':
                        result = self.multiply(num1, num2)
                        op = '*'
                    elif choice == '4':
                        result = self.divide(num1, num2)
                        op = '/'

                    record = f"{num1} {op} {num2} = {result}"
                    self.history.append(record)
                    print(f"\nResult: {record}")

                except ValueError:
                    print("\n[Error] Invalid input. Please enter numeric values.")
                except ZeroDivisionError as e:
                    print(f"\n[Error] {e}")
            else:
                print("\n[Error] Invalid option selected. Please choose between 1 and 6.")

if __name__ == "__main__":
    calc = Calculator()
    calc.run()
    