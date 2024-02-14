"""
Exercise 5:
Write a program that reads 10 numbers and prints the minimum and maximum values read.

(PT-BR)
Exercício 5:
Escreva um programa que leia 10 números e escreva o menor valor lido e o maior valor lido.
"""

num = int(input("Enter a value: "))
maxi = num
mini = num

for i in range(9):
    if i != 0:
        num = int(input("Enter a value: "))
    if num > maxi:
        maxi = num
    elif num < mini:
        mini = num

print(f'Maximum: {maxi}')
print(f'Minimum: {mini}')
