# Exercise 6:
# Create a program that prompts the user to prompt a number.
# Use a loop to continue prompting until the user enters a valid input that can be converted to a number.
# Handle with type conversion errors.

# (PT-BR)
# Exercício 6:
# Crie um programa que solicita ao usuário para inserir um número.
# Use um loop para continuar solicitando até que o usuário insira um valor que possa ser convertido para um número. 
# Lide com erros de conversão de tipo.

def conversion_float(a):
    try:
        return f'Valor: {float(a)}'
    except ValueError:
        while (True):
            try:
                return f'Valor: {float(a)}'
            except ValueError:
                a = input('Enter a value that can be converted to a number:')

num = input('Enter a value that can be converted to a number:')

print(conversion_float(num))
