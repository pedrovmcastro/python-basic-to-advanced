"""
Exercise 10:
Read a 3x3 matrix. Calculate the sum of the elements above the main diagonal, the sum of the elements below the main diagonal, 
and the sum of the elements on the main diagonal.


(PT-BR)
Exercício 10:
Leia uma matriz de 3x3 elementos. Calcule a soma dos elementos que estão acima da diagonal principal, a soma dos
elementos que estão abaixo da diagonal principal, e a soma dos elementos que estão na diagonal principal.
"""

# Matrix input:
matrix = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(int(input(f'[{i},{j}]: ')))
    matrix.append(row)

sum_above, sum_below, sum_diagonal = 0, 0, 0

# Comparing indices:
for i in range(3):
    for j in range(3):
        if j > i:
            sum_above += matrix[i][j]
        elif j < i:
            sum_below += matrix[i][j]
        else:
            sum_diagonal += matrix[i][j]

print('=-'*30)
print(f'SUM ABOVE = {sum_above}\nSUM BELOW = {sum_below}\nSUM DIAGONAL = {sum_diagonal}\n')
