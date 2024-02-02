"""
Example 2:

Suppose I want to flatten a given 2-D list:

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

Expected Output: flatten_matrix = [1, 2, 3, 4, 5, 6, 7, 8, 9]
"""

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flatten_matrix = [val for sublist in matrix for val in sublist]
print(flatten_matrix)

# EXEMPLO 2:

matrix = []

for i in range(3):
    # Append an empty sublist inside the list
    matrix.append([])
    for j in range(3):
        matrix[i].append(j)

print(matrix)

matrix = [[j for j in range(3)] for i in range(3)]
