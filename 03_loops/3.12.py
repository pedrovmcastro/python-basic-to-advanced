"""
Exercise:

(PT-BR)
Exercício:

"""

"""
Faça um programa que leia um número inteiro positivo N e imprima todos os números naturais de N até 0
em ordem decrescente"
"""

N = 0

while N <= 0:
    N = input('Digite um número inteiro positivo: ')
    for i in N:    # i = letra e N[i] = posição da letra
        if i == '.':
            N = 0
            break
    N = int(N)

for i in range(N, -1, -1):
    print(f'{i} ', end='')
