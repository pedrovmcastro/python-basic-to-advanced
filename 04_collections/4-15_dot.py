"""
Exercise 15:
Read two sets of real numbers, store them in arrays, and calculate their dot product.
Both sets have 5 elements each. Print the two sets and the dot product, where the dot product
is given by x1*y1 + x2*y2 + ... + xn*yn.


(PT-BR)
Exercício 15:
Ler dois conjuntos de números reais, armazenando-os em vetores e calcular o produto escalar entre eles.
Os conjuntos têm 5 elementos cada. Imprimir os dois conjuntos e o produto escalar, sendo que o produto escalar
é dado por x1*y1 + x2*y2 + ... + xn*yn
"""

A, B = set(), set()

print('Enter 5 elements for set A (without repeating):')
while len(A) < 5:
    A.add(float(input()))

print('Enter 5 elements for set B (without repeating):')
while len(B) < 5:
    B.add(float(input()))

print('SET A:', A)
print('SET B:', B)

A, B = list(A), list(B)

dot_product = 0
for i, value in enumerate(A):
    dot_product += A[i] * B[i]
print(dot_product)
