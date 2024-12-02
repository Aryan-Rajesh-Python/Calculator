import pyfiglet
import math
import random
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

# Display title
app = pyfiglet.figlet_format("Advanced Calculator")
print(app)

# Define operation functions
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return "Error! Division by zero."
    return n1 / n2

def floor_division(n1, n2):
    if n2 == 0:
        return "Error! Division by zero."
    return n1 // n2

def modulo(n1, n2):
    if n2 == 0:
        return "Error! Division by zero."
    return n1 % n2

def power(n1, n2):
    return n1 ** n2

def square_root(n1):
    if n1 < 0:
        return "Error! Cannot take square root of a negative number."
    return math.sqrt(n1)

def logarithm(n1, base=10):
    if n1 <= 0 or base <= 0:
        return "Error! Invalid input for logarithm."
    return math.log(n1, base)

def trigonometric_functions(n1, function='sin'):
    if function == 'sin':
        return math.sin(math.radians(n1))
    elif function == 'cos':
        return math.cos(math.radians(n1))
    elif function == 'tan':
        return math.tan(math.radians(n1))
    else:
        return "Error! Invalid trigonometric function."

def factorial(n1):
    if n1 < 0:
        return "Error! Cannot take factorial of a negative number."
    if n1 > 170:
        return "Error! Number too large for factorial calculation."
    return math.factorial(int(n1))

# Additional Features
def random_number(min_val, max_val):
    return random.randint(min_val, max_val)

def solve_equation(equation):
    try:
        x = sp.symbols('x')
        eq = sp.sympify(equation)
        solutions = sp.solve(eq, x)
        return solutions
    except Exception as e:
        return f"Error in equation: {e}"

def currency_converter(amount, from_currency, to_currency):
    # This is a mock; replace with actual API call for real-time conversion
    exchange_rates = {
        'USD': {'EUR': 0.85, 'INR': 75, 'GBP': 0.75},
        'EUR': {'USD': 1.18, 'INR': 88, 'GBP': 0.88},
        'INR': {'USD': 0.013, 'EUR': 0.011, 'GBP': 0.011},
        'GBP': {'USD': 1.33, 'EUR': 1.14, 'INR': 98.2}
    }
    if from_currency not in exchange_rates or to_currency not in exchange_rates[from_currency]:
        return "Error! Invalid currency pair."
    return amount * exchange_rates[from_currency][to_currency]

def plot_graph():
    x = np.linspace(-10, 10, 100)
    y = np.sin(x)
    plt.plot(x, y)
    plt.title("Sine Wave")
    plt.xlabel("X")
    plt.ylabel("sin(X)")
    plt.grid(True)
    plt.show()

# Handling complex numbers (e.g., 3+4j)
def complex_operations(n1, n2, operation):
    if operation == "+":
        return n1 + n2
    elif operation == "-":
        return n1 - n2
    elif operation == "*":
        return n1 * n2
    elif operation == "/":
        if n2 == 0:
            return "Error! Division by zero."
        return n1 / n2
    else:
        return "Invalid complex operation."

# Memory feature to store previous results
memory = None

# Function to format and display result
def display_result(result):
    if isinstance(result, float):
        return f"{result:.2f}"  # Format floating-point result to 2 decimal places
    return result

# Function to handle user input with error handling
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

# Function to handle history viewing
def view_history(history):
    if history:
        print("\nCalculation History:")
        for index, calc in enumerate(history, start=1):
            print(f"{index}. {calc}")
    else:
        print("No history available.")

# Main calculator logic
def main():
    global memory
    history = []  # Store calculations history
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide,
        '//': floor_division,
        '%': modulo,
        '**': power,
        'sqrt': square_root,
        'log': logarithm,
        'sin': trigonometric_functions,
        'cos': trigonometric_functions,
        'tan': trigonometric_functions,
        'fact': factorial,
        'rand': random_number,
        'eqn': solve_equation,
        'conv': currency_converter,
        'plot': plot_graph,
        'complex': complex_operations,
    }

    print("Welcome to the Advanced Calculator!")

    while True:
        num1 = get_number("Enter the first number: ")

        while True:
            # Display operation menu
            print("\nSelect an operation:")
            print("+: add")
            print("-: subtract")
            print("*: multiply")
            print("/: divide")
            print("//: floor_division")
            print("%: modulo")
            print("**: power")
            print("sqrt: square_root")
            print("log: logarithm")
            print("sin: trigonometric_functions")
            print("cos: trigonometric_functions")
            print("tan: trigonometric_functions")
            print("fact: factorial")
            print("rand: random_number")
            print("eqn: solve equation (e.g., '2*x + 5 = 0')")
            print("conv: currency_converter (e.g., '100 USD to EUR')")
            print("plot: plot graph")
            print("complex: complex number operations (e.g., '3+4j + 2+3j')")
            print("mem: view memory")
            print("history: view calculation history")
            print("exit: exit the calculator")

            operation_symbol = input("Pick an operation: ").strip().lower()

            if operation_symbol == 'exit':
                print("Thank you for using the calculator!")
                return

            if operation_symbol == 'mem' and memory is not None:
                print(f"Memory: {memory}")
                continue

            if operation_symbol == 'history':
                view_history(history)
                continue

            if operation_symbol in operations:
                if operation_symbol in ['rand', 'eqn', 'conv', 'plot', 'complex']:
                    if operation_symbol == 'rand':
                        min_val = int(input("Enter minimum value: "))
                        max_val = int(input("Enter maximum value: "))
                        result = operations[operation_symbol](min_val, max_val)
                    elif operation_symbol == 'eqn':
                        equation = input("Enter equation to solve (e.g., '2*x + 5 = 0'): ")
                        result = operations[operation_symbol](equation)
                    elif operation_symbol == 'conv':
                        amount = float(input("Enter amount to convert: "))
                        from_currency = input("From currency (e.g., USD): ").upper()
                        to_currency = input("To currency (e.g., EUR): ").upper()
                        result = operations[operation_symbol](amount, from_currency, to_currency)
                    elif operation_symbol == 'plot':
                        operations[operation_symbol]()
                        result = "Graph displayed."
                    else:  # 'complex'
                        comp_num1 = complex(input("Enter first complex number (e.g., 3+4j): "))
                        comp_num2 = complex(input("Enter second complex number (e.g., 2+3j): "))
                        operation = input("Enter operation (+, -, *, /): ").strip()
                        result = operations[operation_symbol](comp_num1, comp_num2, operation)
                else:
                    num2 = get_number("Enter the next number: ")
                    result = operations[operation_symbol](num1, num2)
                
                print(f"Result: {display_result(result)}")
                memory = result  # Store the result in memory
                history.append(f"{num1} {operation_symbol} {num2 if operation_symbol not in ['rand', 'eqn', 'conv', 'plot', 'complex'] else ''} = {result}")
                
                opinion = input("Do you want to continue with the calculation (yes/no)? ").strip().lower()

                if opinion == "yes":
                    num1 = result
                else:
                    print("Thank you for using the calculator!")
                    return

            else:
                print("Invalid operation! Please choose a valid operation.")
                continue

if __name__ == "__main__":
    main()
