# Exercise 4:
# Ask the user to enter a simple mathematical expression (e.g., "2 + 3").
# Try to evaluate the expression and print the result. Use a try-except block to handle evaluation errors.

# (PT-BR)
# Exercício 4:
# Peça ao usuário para inserir uma expressão matemática simples (por exemplo, "2 + 3"). 
# Tente avaliar a expressão e imprimir o resultado. Use um bloco try-except para lidar com erros de avaliação.


def operacao(exp):
    op = ['+', '-', '*', '/']
    exp = exp.split(" ")
    if len(exp) > 3:
        return 'Error: Enter an expression with a maximum of two operands.'
    if exp[1] not in op:
        return 'Error: Enter a basic operation: +, -, *, or /'
    
    if exp[1] == '+':
        return f"Result: {int(exp[0]) + int(exp[2])}"
    elif exp[1] == '-':
        return f"Result: {int(exp[0]) - int(exp[2])}"
    elif exp[1] == '*':
        return f"Result: {int(exp[0]) * int(exp[2])}"
    else:
        return f"Result: {int(exp[0]) / int(exp[2])}"
    

exp = input("Enter a mathematical expression (e.g., '2 + 3'): ")
try:
    print(operacao(exp))
except IndexError:
    print('Error: enter a simple expression separated with spaces, e.g: 2 + 3.')
except ValueError:
    print('Error: the operands must be integers.')
except ZeroDivisionError:
    print('Zero division error.')
