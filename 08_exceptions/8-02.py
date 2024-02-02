# Exercise 2:
# Create a list of numbers. Ask the user for an index and try to access the corresponding element in the list.
# Use a try-except block to handle indices that are out of range.

# (PT-BR)
# Exercício 2:
# Crie uma lista de números. Solicite ao usuário um índice e tente acessar o elemento correspondente na lista. 
# Use um bloco try-except para lidar com índices fora do intervalo.

lista = [2, 7, 21, 30, 55]
try:
    print(f'Value: {lista[int(input('Enter an index: '))]}')
except IndexError as err:
    print(f'IndexError: {err}')
