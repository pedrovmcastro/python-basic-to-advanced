"""
Exercise:

(PT-BR)
Exercício:

"""
"""Ler dois conjuntos de números reais, armazenando-os em vetores e calcular o produto escalar entre eles.
Os conjuntos têm 5 elementos cada. Imprimir os dois conjuntos e o produto escalar, sendo que o produto escalar
é dado por x1*y1 + x2*y2 + ... + xn*yn"""

A, B = set(), set()

print('Digite 5 elementos para o conjunto A (sem repetir):')
while len(A) < 5:
    A.add(float(input()))

print('Digite 5 elementos para o conjunto B (sem repetir):')
while len(B) < 5:
    B.add(float(input()))

print('CONJUNTO A:', A)
print('CONJUNTO B:', B)

A, B = list(A), list(B)

produto_escalar = 0
for i, valor in enumerate(A):
    produto_escalar += A[i]*B[i]
print(produto_escalar)
