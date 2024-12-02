import os
from art import logo

print (logo)

def add(n1, n2):
    return n1 + n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2

operations = {
    "+":add,
    "-":sub,
    "*":mul,
    "/":div
}
def clear_console():
    print("\n" * 100)

def calculator():
    num1 = float(input("What is the first number?: \n"))
    while True:
        for symbol in operations:
            print (symbol)
        operation_symbol = input("Pick an operation: \n")
        num2 = float(input("What is the next number?: \n"))
        calculation_operation = operations[operation_symbol](num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {calculation_operation}")

        choice = input(f"Type 'y' to continue calculating with {calculation_operation}, or type 'n' to start a new calculation or 's' to stop calculations: ").lower()
        if choice == "y":
            num1 = calculation_operation
        elif choice =="n":
            clear_console()
            calculator()
        elif choice == "s":
            print("Goodbye!")
            break
        else:
            print("Invalid input. Exiting the program.")
            break

calculator()

