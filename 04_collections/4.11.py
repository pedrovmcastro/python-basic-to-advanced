"""
Faça um programa que receba do usuário dois vetores, A e B, com 10 números inteiros cada.
Crie um vetor denominado C calculando C = A - B. Mostre na tela os dados do vetor C
"""

A, B, C = [], [], []

print('Digite os valores do vetor A:')
for _ in range(10):
    A.append(int(input()))

print('Digite os valores do vetor B:')
for _ in range(10):
    B.append(int(input()))

for valor in A:
    if valor in A and valor not in B:
        C.append(valor)

print(C, end='')
