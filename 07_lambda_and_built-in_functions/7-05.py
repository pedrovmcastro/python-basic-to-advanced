# Exercise 5:
# Sort a list of dictionaries based on a specific value from each dictionary using the sorted function.

# (PT-BR)
# Exercício 5:
# Ordene uma lista de dicionários com base em um valor específico de cada dicionário usando a função sorted.

people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Carol", "age": 35},
    {"name": "David", "age": 28},
]
print(sorted(people, key=lambda x: x["age"]))
