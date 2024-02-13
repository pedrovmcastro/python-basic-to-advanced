"""
Exercise:

(PT-BR)
Exercício:

"""

"""
Escreva um algoritmo que leia um número inteiro entre 100 e 999
e imprima na saída cada um dos algarismos que compõe o número
"""

N = 0

while not (99 < N < 1000):
    N = int(input('Digite um numero entre 100 e 999: '))

N = str(N)

for i in N:
    print(i)
