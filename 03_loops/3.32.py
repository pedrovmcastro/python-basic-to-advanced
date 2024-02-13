"""
Exercise:

(PT-BR)
Exercício:

"""

"""
Faça um programa que simula o lançamento de dois dados, d1 e d2,
n vezes, e tem como saída o número de cada dado e a relação entre
eles (>,<,=) de cada lançamento.
"""
n = int(input('Vai fazer quantos lançamentos? '))
d1, d2 = 0, 0

for i in range(n):
    while d1 < 1 or d1 > 6:
        d1 = int(input('Digite o valor do primeiro dado: '))
    while d2 < 1 or d2 > 6:
        d2 = int(input('Digite o valor do segundo dado: '))

    if d1 < d2:
        print('d1 < d2')
    elif d1 > d2:
        print('d1 > d2')
    else:
        print('d1 = d2')

    d1, d2 = 0, 0
