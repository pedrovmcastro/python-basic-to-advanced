"""
Exercise 2:
Implement a program that prompts the user for a number. If this number is positive, calculate its square root. 
If the number is negative, display a message stating that the number is invalid. 

Exercício 2 (PT-BR):
Leia um número fornecido pelo usuário. Se esse número for positivo, calcule a raiz quadrada do número.
Se o número for negativo, mostre uma mensagem dizendo que o número é inválido.
"""
import math

num = float(input("Enter a number: "))

if num % 2 == 0:
    print(math.sqrt(num))
else:
    print("Invalid number.")
