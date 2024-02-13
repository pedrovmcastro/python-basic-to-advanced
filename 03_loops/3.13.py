"""
Exercise:

(PT-BR)
Exercício:

"""

"""
Faça um programa que leia um número inteiro positivo N e imprima todos os números naturais
pares de 0 até N em ordem crescente.
"""

N = 0

while N <= 0:
    N = input('Digite um número inteiro positivo: ')
    for i in N:    # i = letra e N[i] = posição da letra
        if i == '.':
            N = 0
            break
    N = int(N)

for i in range(0, N+1, 2):
    print(f'{i} ', end='')
