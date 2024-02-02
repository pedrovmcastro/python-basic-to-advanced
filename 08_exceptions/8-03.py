# Exercise 3:
# Ask the user to input two numbers.
# Try to divide the first number by the second.
# Handle errors such as division by zero, incorrect values, and other unspecified errors. Print appropriate messages for each type of error.

# (PT-BR)
# Exercício 3:
# Peça ao usuário para inserir dois números.
# Tente dividir o primeiro pelo segundo.
# Trate os erros de divisão por zero, valores incorretos e outros erros não especificados. Imprima mensagens apropriadas para cada tipo de erro.


def division(a, b):
    try:
        return float(a)/float(b)
    except ValueError:
        return 'Error: Invalid input.'
    except ZeroDivisionError:
        return 'Zero Division Error.'
        
        
print('Enter two numbers:')
n1, n2 = input(), input()

print(f'Result: {division(n1, n2)}')
