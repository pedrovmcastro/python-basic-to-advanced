"""
Exercise 3:
Using list comprehensions, and the list fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']:
a) Make a list that contains each fruit with more than 5 characters;
b) Make a list that contains each fruit with exactly 5 characters;
c) Make a list that contains fruits that have less than 5 characters.
d) Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]


(PT-BR)
Exercício 3:
Usando list comprehensions e a lista fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']:
a) Crie uma lista que contenha cada fruta com mais de 5 caracteres;
b) Crie uma lista que contenha cada fruta com exatamente 5 caracteres;
c) Crie uma lista que contenha frutas com menos de 5 caracteres.
d) Crie uma lista contendo o número de caracteres em cada fruta. A saída seria [5, 4, 10, etc...]
"""

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

# a)
fruits_more_than_5_char = [fruit for fruit in fruits if len(fruit) > 5]
print(f'Fruits with more than 5 characters: {fruits_more_than_5_char}')

# b)
fruits_with_5_char = [fruit for fruit in fruits if len(fruit) == 5]
print(f'Fruits with 5 characters: {fruits_with_5_char}')

# c)
fruits_fewer_than_5_char = [fruit for fruit in fruits if len(fruit) < 5]
print(f'Fruits with fewer than 5 characters: {fruits_fewer_than_5_char}')

# d)
print(f'Lenght: {[len(fruit) for fruit in fruits]}')
