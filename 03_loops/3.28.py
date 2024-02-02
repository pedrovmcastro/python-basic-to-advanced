"""
Faça um programa que leia um valor N inteiro e positivo, calcule
e mostre o valor de E, conforme a fórmula a seguir:

E = 1 + 1/1! + 1/2! + 1/3! + ... 1/N!
"""

inteiro, positivo = False, False

while not (inteiro and positivo):
    N = input('Digite um número inteiro positivo: ')
    if N.isdigit():
        inteiro = True
        N = int(N)
        if N > 0:
            positivo = True

fat, E = 1, 0
for i in range(1, N+1):
    for j in range(i, 0, -1):
        fat *= j
    E += 1/fat
    fat = 1











