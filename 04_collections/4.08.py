"""
Faça um programa que leia um vetor de 10 posições e verifique se existem valores iguais e os escreva na tela.
"""

vet, iguais = [], []

for _ in range(10):
    vet.append(int(input()))

for valor1 in vet:
    if str(valor1) in iguais:
        continue
    for valor2 in vet[vet.index(valor1)+1:]:
        if valor1 == valor2:
            iguais.append(str(valor1))
            break

print(f"Valores iguais = {', '.join(iguais)}")
