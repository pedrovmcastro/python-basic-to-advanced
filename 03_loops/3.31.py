"""
Exercise:

(PT-BR)
Exercício:

"""

"""
Faça um programa que calcule e escreva o valor de S

S = 1/1 + 3/2 + 5/3 + 7/4 + ... + 99/50
"""

k, S = 0, 0

for i in range(1, 100, 2):
    k += 1
    S += i/k
