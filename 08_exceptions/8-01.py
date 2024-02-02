# Exercise 1:
# Ask the user to enter a number. Attempt to convert the input to an integer.
# If the conversion fails, inform the user that the entered value is not an integer.

# (PT-BR)
# Exercício 1:
# Peça ao usuário para inserir um número. Tente converter a entrada para um número inteiro. 
# Se a conversão falhar, informe ao usuário que o valor inserido não é um número inteiro.

try:
    print(f'Number: {int(input('Enter an integer: '))}')
except ValueError:
    print('ValueError: the value entered is not an integer.')
