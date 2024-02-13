"""
Exercise:

(PT-BR)
Exercício:

"""
"""
Leia um vetor de 10 posições.
Contar e escrever quantos valores pares ele possui.
"""

vet = []
for i in range(10):
    N = int(input())
    vet.append(N)

cont = 0
for valor in vet:
    if valor % 2 == 0:
        cont += 1

print(cont)
