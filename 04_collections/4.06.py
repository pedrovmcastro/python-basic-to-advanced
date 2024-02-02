"""
Faça um programa que receba do usuário um vetor com 10 posições.
Em seguida deverá ser impresso o maior e o menor elemento do vetor.
"""

vet = []

for i in range(10):
    N = int(input())
    vet.append(N)

maior = menor = vet[0]

for valor in vet[1:]:
    if valor > maior:
        maior = valor
    if valor < menor:
        menor = valor

print(f'MAIOR = {maior}\nMENOR = {menor}')
