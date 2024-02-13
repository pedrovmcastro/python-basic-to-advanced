"""
Exercise:

(PT-BR)
Exercício:

"""
fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

# Exercise 5 - make a list that contains each fruit with more than 5 characters
fruits_more_than_5_char = [fruit for fruit in fruits if len(fruit) > 5]
print(f'frutas com mais de 5 caracteres: {fruits_more_than_5_char}')

# Exercise 6 - make a list that contains each fruit with exactly 5 characters
fruits_with_5_char = [fruit for fruit in fruits if len(fruit) == 5]
print(f'frutas com 5 caracteres: {fruits_with_5_char}')

# Exercise 7 - Make a list that contains fruits that have less than 5 characters
fruits_minus_than_5_char = [fruit for fruit in fruits if len(fruit) < 5]
print(f'frutas com menos de 5 caracteres: {fruits_minus_than_5_char}')
