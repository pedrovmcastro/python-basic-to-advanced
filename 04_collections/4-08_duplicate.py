"""
Exercise 8:
Read an array with 10 integer numbers. Write the elements of the array, eliminating duplicate elements.


(PT-BR)
Exercício 8:
Leia um vetor com 10 números inteiros. Escreva os elementos do vetor eliminando elementos repetidos.
"""

arr, no_duplicates = [], []

for _ in range(10):
    arr.append(int(input()))

for value in arr:
    if str(value) not in no_duplicates:
        no_duplicates.append(str(value))

print(', '.join(no_duplicates))
