"""
Faça um programa que leia um número inteiro positivo ímpar N e imprima todos
os números ímpares de 1 até N em ordem crescente.
"""

inteiro, positivo, impar = False, False, False

while not (inteiro and positivo and impar):
    N = input('Digite um número inteiro positivo impar: ')
    if N.isdigit():
        inteiro = True
        N = int(N)
        if N > 0 and N % 2 != 0:
            positivo, impar = True, True

for i in range(1, N+1, 2):
    print(f'{i} ', end='')


