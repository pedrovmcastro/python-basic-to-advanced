"""
Exercise 12:
Write a program that reads a text file containing the name and price of various products (separated per line),
and calculates the total purchase amount.

(PT-BR)
Exercício 12:
Faça um programa que leia um arquivo contendo o nome e o preço de diversos produtos (separados por linha),
e calcule o total da compra.
"""

products = {}
lines = 0

with open('products.txt') as file:
    for line in file:  
        lines += 1
    file.seek(0)
    for _ in range(lines):
        line = file.readline()
        product, price = line.split()
        products[product] = price

total = 0
for value in product.values():
    total += int(value)

print(total)
