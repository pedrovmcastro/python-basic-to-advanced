"""
Exercise:

(PT-BR)
Exercício:

"""

"""
Faça um algoritmo que encontre o primeiro múltiplo de 11, 13 ou 17
após um número dado.
"""

N = int(input('Digite um numero: '))

while True:
    if N % 11 == 0 or N % 13 == 0 or N % 17 == 0:
        print(N)
        break
    N += 1

