"""
Exercise:

(PT-BR)
Exercício:

"""

""""
Escreva um programa para calcular o valor da série, para 5 termos.
S = 0 + 1/2! + 1/4! + 1/6! + 1/8!
"""

fat, S = 1, 0
for i in range(2, 9, 2):
    for j in range(i, 0, -1):
        fat *= j
    S += 1/fat
    fat = 1
