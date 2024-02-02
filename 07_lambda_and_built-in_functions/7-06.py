# Exercise 6:
# Create a lambda function that returns the square of a number and use it to map the square of all elements in a list.

# (PT-BR)
# Exercício 6:
# Crie uma função lambda que retorne o quadrado de um número e use-a para mapear o quadrado de todos os elementos em uma lista.

lista = [1, 2, 3, 4, 5]
print(list(map(lambda x: x**2, lista)))
