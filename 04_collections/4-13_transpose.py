"""
Exercise 13:
Read a 3x3 matrix. Calculate and print its transpose.

(PT-BR)
Exercício 13:
Leia uma matriz de 3x3 elementos. Calcule e imprima a sua transposta
"""

# Matrix input:
matrix = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(int(input(f'[{i},{j}]: ')))
    matrix.append(row)

transposed_matrix = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(matrix[j][i])
    transposed_matrix.append(row)

print('-='*30)
print('Transposed Matrix:')
for i in range(3):
    for j in range(3):
        print(f'[{transposed_matrix[i][j]:5^}]', end='')
    print()
