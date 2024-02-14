"""
Exercise 3:
Implement a program that prompts the user to enter 10 values, calculates their sum, and displays it on the screen.


(PT-BR)
Exercício 3:
Faça um programa que peça ao usuário para digitar 10 valores e some-os. Imprima a soma na tela.
"""

sum = 0
for i in range(9):
    n = int(input("Enter a value: "))
    sum += n

print(sum)
