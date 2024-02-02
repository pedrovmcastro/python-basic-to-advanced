"""
Faça um programa que leia um numero indeterminado de idades de individuos (pare quando for informada a idade 0),
e calcule a idade media desse grupo.
"""

soma, cont = 0, 0

while True:
    idade = int(input('Digite uma idade: '))
    if idade <= 0:
        break
    soma += idade
    cont += 1

print('Idade media:', soma/cont)
