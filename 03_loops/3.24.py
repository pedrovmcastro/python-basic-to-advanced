"""
Escreva um programa que leia um número inteiro e calcule a soma
de todos os divisores desse número, com exceção dele próprio.
Ex: a soma dos divisores do número 66 é 1+2+3+6+11+22+33=78
"""

N, soma = 0, 0

while N <= 0:
    N = int(input('Digite um numero positivo: '))

for i in range(1, N):
    if N % i == 0:
        soma += i

print(soma)
