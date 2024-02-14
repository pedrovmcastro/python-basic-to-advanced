"""
Exercise 20:
Consider an array A with 11 elements where A1 < A2 < ... < A6 > A7 > A8 > ... > A11,
meaning it is sorted in ascending order up to the sixth element and, from that point onward,
it is sorted in descending order. Propose an algorithm to sort the elements.

(PT-BR)
Exercício 20:
Considere um vetor A com 11 elementos onde A1 < A2 < ... < A6 > A7 > A8 > ... > A11, ou seja, está
ordenado em ordem crescente até o sexto elemento, e a partir desse elemento está ordenado em ordem decrescente.
Proponha um algoritmo para ordenar os elementos.
"""

A, B = [], []

for _ in range(11):
    A.append(int(input()))

A.sort()

for value in A[6:]:
    B.append(value)
    A.remove(value)

B.sort(reverse=True)

A += B

print(A)
