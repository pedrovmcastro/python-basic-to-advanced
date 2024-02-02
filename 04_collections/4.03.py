"""
ler um conjunto de números reais, armazenando-os em vetor e calcular o quadrado
das componentes deste vetor, armazenando o resultado em outro vetor.
os conjuntos têm 10 elementos cada. imprimir todos os conjuntos.
"""

vet1, vet2 = [], []

for i in range(10):
    N = float(input())
    vet1.append(N)

for valor in vet1:
    valor **= 2
    vet2.append(valor)

print(vet1)
print(vet2)
