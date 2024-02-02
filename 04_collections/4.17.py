"""
Faça um programa que leia dois vetores de 10 posições e calcule outro vetor contendo, nas posições pares os valores
do primeiro e nas posições impares os valores do segundo.
"""

vet1, vet2, vetRes = [], [], []

for _ in range(10):
    vet1.append(input())

for _ in range(10):
    vet2.append(input())

x = y = 0
for i in range(20):
    if i % 2 == 0:
        vetRes.append(vet1[x])
        x += 1
    else:
        vetRes.append(vet2[y])
        y += 1

for valor in vetRes:
    print(valor)
