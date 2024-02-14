"""
Exercise 8:
Create a program that presents the user with a menu containing 4 options of mathematical operations (the basic ones, for example). 
The user chooses one of the options, and your program then prompts for two numerical values, performs the operation, displays the result, and exits.

Exercício 8 (PT-BR):
Faça um programa que mostre ao usuário um menu com 4 opções de operações matemáticas (as básicas, por exemplo).
O usuário escolhe uma das opções e o seu programa então pede dois valores numéricos e realiza a operação, mostrando o resultado e saindo.
"""

print("-="*10 + " BASIC OPERATIONS " + "-="*10)
print("|" + " "*21 + "+, -, * or /. " +  " "*21 + "|")
print("-="*29)

op = input("Operation: ")

if op in "+-*/":
    num1 = float(input("Enter the first numerical value: "))
    num2 = float(input("Enter the second numerical value: "))
    match op:
        case "+":
            print(f"Result: {(num1 + num2):.2f}")
        case "-":
            print(f"Result: {(num1 - num2):.2f}")
        case "*":
            print(f"Result: {(num1 * num2):.2f}")
        case "/":
            print(f"Result: {(num1 / num2):.2f}")
else:
    print("Invalid operation.")