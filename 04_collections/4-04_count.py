"""
Exercise 4:
Read an array of 10 positions. Count and write how many even values it contains.

(PT-BR)
Exercício 4:
Leia um vetor de 10 posições.
Contar e escrever quantos valores pares ele possui.
"""

vet = []
for i in range(10):
    N = int(input())
    vet.append(N)

count = 0
for valor in vet:
    if valor % 2 == 0:
        count += 1

print(count)
