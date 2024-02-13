"""
Exercise:

(PT-BR)
Exercício:

"""
# Exercício 17:
# Cria uma função que aceite argumentos da linha de comando, posicionais e nomeados, 
# e imprimir ambos os argumentos posicionais e nomeados.

def print_arguments_and_keyarguments(*args, **kwargs):
    print('Posicionais:')
    if len(args) == 0:
        print('(nenhum)')
    for arg in args:
        print(arg)
    print('Nomeados:')
    if len(kwargs) == 0:
        print('(nenhum)')
    for key, value in kwargs.items():
        print(f'{key}:{value}')

# Testando:
print(f'Teste 1.\n{'-='*30}')
print_arguments_and_keyarguments(1, 2)

print(f'\nTeste 2.\n{'-='*30}')
print_arguments_and_keyarguments(a=1, b=2)

print(f'\nTeste 3.\n{'-='*30}')
print_arguments_and_keyarguments(3, 4, d=5, c=3)
