import pyfiglet
app=pyfiglet.figlet_format("Simple Calculator")
print(app)
def add(n1, n2):
  return n1 + n2
def subtract(n1, n2):
  return n1 - n2
def multiply(n1, n2):
  return n1 * n2
def divide(n1, n2):
  return n1 / n2
def floor_division(n1, n2):
  return n1 // n2
def modulo(n1, n2):
  return n1 % n2
def power(n1, n2):
  return n1 ** n2
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
  "//": floor_division,
  "%": modulo,
  "**": power
}
def calculator():
  num1 = float(input("Enter the first number: "))
  while (True):
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("Enter a number: "))
    function1 = operations[operation_symbol]
    answer = function1(num1,num2)
    print(f"{answer}")
    opinion=input("Do you want to continue with the calculation: ")
    if (opinion=="yes" or opinion=="Yes" or opinion=="YES"):
        num1 = answer
    else:
        print("Thank you for using our calculator app")
calculator()
