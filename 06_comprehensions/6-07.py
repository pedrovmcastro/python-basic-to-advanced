"""
Exercise:

(PT-BR)
Exercício:

"""
"""
Exercise 11: Transposing a Matrix
Transpose a matrix using a nested list comprehension.
"""

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

trans_matrix = [[linha[i] for linha in matrix] for i in range(3)]
print(trans_matrix)
