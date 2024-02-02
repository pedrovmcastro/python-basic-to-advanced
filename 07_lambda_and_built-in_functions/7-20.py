# Exercise 20:
# Write a program that uses the zip function to create a list of tuples, where each tuple contains the name of a product and its price with a 10% discount.

# (PT-BR)
# Exercício 20:
# Escreva um programa que use a função zip para criar uma lista de tuplas, onde cada tupla contém o nome de um produto 
# e o seu preço com desconto de 10%.

# Example input
products = ["Rice", "Beans", "Pasta", "Meat", "Milk"]
prices = [5.00, 4.50, 3.00, 25.00, 3.50]

# Example output
# result_list = [("Rice", 4.50), ("Beans", 4.05), ("Pasta", 2.70), ("Meat", 22.50), ("Milk", 3.15)]

discounted_prices = [price - price * 0.1 for price in prices]
print(discounted_prices)

result_list = list(zip(products, discounted_prices))
print(result_list)

# More direct way:
print(list(zip(products, [price - price * 0.1 for price in prices])))
