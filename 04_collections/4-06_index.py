"""
Exercise 6:
Create a program to read 10 values and then show the position(s) where the maximum and minimum values are located. 
If there are multiple occurrences of the maximum or minimum value, show all positions.

(PT-BR)
Exercício 6:
Fazer um programa para ler 10 valores e, em seguida, mostrar a posição
onde se encontram o maior e o menor valor (caso haja mais de uma ocorrência do maior ou menor valor,
mostrar todas posições).
"""

lista, ind_max, ind_min = [], [], []

for _ in range(10):
    lista.append(int(input()))

for i, value in enumerate(lista):
    if value == max(lista):
        ind_max.append(str(i))
    if value == min(lista):
        ind_min.append(str(i))

print(f'Maximum: {max(lista)}\nPosition(s): {", ".join(ind_max)}')
print(f'Minimum: {min(lista)}\nPosition(s): {", ".join(ind_min)}')
