"""
Exercise:

(PT-BR)
Exercício:

"""

"""
Faça um programa que leia um conjunto não determinado de valores, um de cada vez,
e escreva para cada um dos valores lidos, o quadrado, o cubo e a raiz quadrada.
Finalize a entrada de dados com um valor negativo ou zero.
"""
import math

while True:
    N = int(input('Digite um valor: '))
    if N <= 0:
        break
    print('Quadrado:', N**2)
    print('Cubo:', N**3)
    print('Raiz quadrada:', math.sqrt(N))
