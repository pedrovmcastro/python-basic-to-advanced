"""
Escreva um programa que leia números inteiros no intervalo [0,50] e os armazene em um vetor de 10 posições.
Preencha um segundo vetor apenas com os números ímpares do primeiro vetor.
Imprima os dois vetores, 2 elementos por linha.
"""

vet1, vet2, i = [], [], 0

while i < 10:
    n = int(input())
    if 0 <= n <= 50:
        vet1.append(n)
        i += 1
    else:
        print('Entrada inválida. Digite um número inteiro entre 0 e 50.')

for valor in vet1:
    if valor % 2 != 0:
        vet2.append(valor)

print('Vetor 1:')
for i in range(0, len(vet1), 2):
    if i + 1 < len(vet1):
        print(vet1[i], vet1[i+1])
    else:
        print(vet1[i])

print('Vetor 2:')
for i in range(0, len(vet2), 2):
    if i + 1 < len(vet2):
        print(vet2[i], vet2[i+1])
    else:
        print(vet2[i])
