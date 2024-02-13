"""
Exercise:

(PT-BR)
Exercício:

"""
"""Escreva um programa que leia 10 números e escreva o menor valor lido e o maior valor lido."""

num = int(input())
maior = num
menor = num

for i in range(9):
    if i != 0:
        num = int(input())
    if num > maior:
        maior = num
    elif num < menor:
        menor = num

print(f'Maior = {maior}')
print(f'Menor = {menor}')
