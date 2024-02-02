"""
Faça um programa que leia um vetor de 8 posições e, em seguida,
leia também dois valores X e Y quaisquer correspondentes a duas
posições no vetor. Ao final seu programa deverá escrever a soma
dos valores encontrados nas respectivas posições X e Y.
"""

vet = []

for i in range(8):
    N = int(input())
    vet.append(N)

X, Y = int(input()), int(input())

soma = vet[X] + vet[Y]

print(soma)
