"""
Considere um vetor A com 11 elementos onde A1 < A2 < ... < A6 > A7 > A8 > ... > A11, ou seja, está
ordenado em ordem crescente até o sexto elemento, e a partir desse elemento está ordenado em ordem decrescente.
Proponha um algoritmo para ordenar os elementos.
"""

A, B = [], []

for _ in range(11):
    A.append(int(input()))

A.sort()

for valor in A[6:]:
    B.append(valor)
    A.remove(valor)

B.sort(reverse=True)

A += B

print(A)
