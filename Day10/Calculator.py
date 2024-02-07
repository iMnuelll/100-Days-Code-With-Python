# Calculator
from art import logo
import os

def add(num1, num2) :
    return num1 + num2
def subtract(num1, num2) :
    return num1 - num2
def multiply (num1, num2) :
    return num1 * num2
def divide (num1, num2) :
    return num1 / num2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

def calculator() :
    print(logo)
    num1 = float(input("What's the first number? "))
    for ops in operations :
        print(ops)

    repeat = "y"
    while repeat == "y" :
        operation_symbol = input("Pick an operation : ")
        num2 = float(input("What's the next number? "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        repeat = input(f"Type 'y'' to continue calculating with {answer}, or type 'n' to start a new calculation : ")
        if repeat == "y" :
            num1 = answer
        else :
            os.system('cls||clear')
            calculator()
calculator()