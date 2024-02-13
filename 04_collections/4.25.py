"""
Exercise:

(PT-BR)
Exercício:

"""
"""Leia uma matriz 4x4, conte e escreva quantos valores maiores que 10 ela possui."""
matriz, count = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], 0
for i in range(4):
    for j in range(4):
        matriz[i][j] = int(input())
for i in range(4):
    for j in range(4):
        if matriz[i][j] > 10:
            count += 1
print(count)
