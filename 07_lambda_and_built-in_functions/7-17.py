# Exercise 17:
# Write a program that uses the zip function to transpose a matrix, i.e., swap the rows with the columns.

# (PT-BR)
# Exercício 17:
# Escreva um programa que use a função zip para transpor uma matriz, ou seja, trocar as linhas pelas colunas.

# Example input
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transposed = list(zip(*matrix))

for row in transposed:
    for x in row:
        print(f'{x} ', end='')
    print()
