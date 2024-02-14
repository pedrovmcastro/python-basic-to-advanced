"""
Exercise 14:
Generate numbers automatically between 0 and 99 for a bingo card. Each card should contain 5 rows of 5 numbers,
and the data should be generated in a way that there are no repeated numbers within the cards. The program should
display the generated card on the screen.

(PT-BR)
Exercício 14:
Faça um programa para gerar automaticamente números entre 0 e 99 de uma cartela de bingo. Sabendo que
cada cartela deverá conter 5 linhas de 5 números, gere estes dados de modo a não ter números repetidos dentro das
cartelas. O programa deve exibir na tela a cartela gerada
"""

import random

bingo_set = set()

# Generate a set of 25 non-repeating numbers
while len(bingo_set) < 25:
    bingo_set.add(random.randint(0, 99))

bingo_list = list(bingo_set)
random.shuffle(bingo_list)

bingo_matrix = []
k = 0

# Create a 5x5 matrix using the generated numbers
for _ in range(5):
    row = []
    for _ in range(5):
        row.append(bingo_list[k])
        k += 1
    bingo_matrix.append(row)

# Display the generated bingo card
for i in range(5):
    for j in range(5):
        print(f'[{bingo_matrix[i][j]:^5}]', end='')
    print()

