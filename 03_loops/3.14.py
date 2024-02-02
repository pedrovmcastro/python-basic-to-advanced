""""
Faça um programa que leia um número inteiro positivo par N
e imprima todos os números pares de 0 até N em ordem crescente.
"""

positivo, inteiro, par = False, False, False

while not (positivo and inteiro and par):
    # também pode ser: while not (positivo, inteiro, par), são equivalentes.
    N = input('Digite um número inteiro positivo par: ')
    for i in N:    # i = letra e N[i] = posição da letra
        if i == '.':
            inteiro = False
            break
    N = int(N)
    inteiro = True

    if N > 0 and N % 2 == 0:
        positivo, par = True, True

for i in range(0, N+1, 2):
    print(f'{i} ', end='')

"""
while not (positivo and inteiro and par):
    numero = int(input("Digite um número inteiro: "))

    positivo = numero > 0
    inteiro = isinstance(numero, int)
    par = numero % 2 == 0

    # Se positivo, inteiro e par forem True, o loop será encerrado
"""
