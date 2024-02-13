"""
Exercise:

(PT-BR)
Exercício:

"""

"""
Escreva um programa que leia um numero inteiro positivo n e em seguida imprima n
linhas do chamado Triangulo de Floyd. Para n = 6, temos:

1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
16 17 18 19 20 21
"""

n = int(input('Digite um numero inteiro positivo: '))
k = 1

for i in range(1, n+1):
    for j in range(k, k+i):
        print(f'{j} ', end='')
    print()
    k += i
