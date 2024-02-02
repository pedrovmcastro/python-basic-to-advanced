"""
Leia um vetor com 20 números inteiros. Escreva os elementos do vetor eliminando elementos repetidos.
"""

vet, nao_repetidos = [], []

for _ in range(10):
    vet.append(int(input()))

for valor in vet:
    if str(valor) not in nao_repetidos:
        nao_repetidos.append(str(valor))

print(', '.join(nao_repetidos))
