"""
Exercise 6: Transposing a Matrix
Transpose a matrix using a nested list comprehension.


(PT-BR)
Exercício 6:
Faça a transposta de uma matriz usando list comprehension aninhadas.
"""

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

transposed_matrix = [[row[i] for row in matrix] for i in range(3)]
print(transposed_matrix)
