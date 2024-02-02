# Exercise 4:
# Create a lambda function that returns True if a number is even and False otherwise. 
# Use this function to filter the even numbers in a list.

# (PT-BR)
# Exercício 4:
# Crie uma função lambda que retorne True se um número for par e False caso contrário. 
# Use essa função para filtrar os números pares em uma lista.

lista = [1, 2, 3, 4, 5, 6, 7, 8]
print(list(filter(lambda x: True if x % 2 == 0 else False, lista)))
