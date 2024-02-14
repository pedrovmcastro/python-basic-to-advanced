"""
Exercise 12:
Read a 3x3 matrix. Calculate the sum of the elements on the secondary diagonal.


(PT-BR)
Exercício 12:
Leia uma matriz de 3x3 elementos. Calcule a soma dos elementos que estão na diagonal secundária
"""

# Matrix input:
matrix = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(int(input(f'[{i},{j}]: ')))
    matrix.append(row)

# Search for the secondary diagonal:
i, j, sum_diagonal = 0, 2, 0
while i <= 2:
    sum_diagonal += matrix[i][j]
    i += 1
    j -= 1

print('=-'*30)
print(f'SUM OF THE SECONDARY DIAGONAL = {sum_diagonal}\n')
