"""
Exercise 13:
Write a program that reads a positive integer n and then prints n lines of the so-called Floyd's Triangle. 
For n = 6, we have:

1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
16 17 18 19 20 21

(PT-BR)
Exercício 13:
Escreva um programa que leia um numero inteiro positivo n e em seguida imprima n
linhas do chamado Triangulo de Floyd. Para n = 6, temos:

1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
16 17 18 19 20 21
"""

n = int(input('Enter a positive integer: '))
k = 1

for i in range(1, n+1):
    for j in range(k, k+i):
        print(f'{j} ', end='')
    print()
    k += i
    