# Exercise 16:
# Write a program that uses the zip function to create a dictionary from two lists,
# where the keys are the country names and the values are their capitals.

# (PT-BR)
# Exercício 16:
# Escreva um programa que use a função zip para criar um dicionário a partir de duas listas,
# onde as chaves são os nomes dos países e os valores são as suas capitais.

# Example input
countries = ["Brazil", "Argentina", "Chile", "Colombia", "Peru"]
capitals = ["Brasília", "Buenos Aires", "Santiago", "Bogotá", "Lima"]

dict1 = dict(zip(countries, capitals))

print(f'dicionary = {dict1}')
