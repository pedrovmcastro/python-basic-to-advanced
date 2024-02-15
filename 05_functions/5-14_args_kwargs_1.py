"""
Exercise 14:
Create a function that accepts command line arguments, both positional and keyword arguments, 
and prints both positional and keyword arguments.


(PT-BR)
Exercício 14:
Cria uma função que aceite argumentos da linha de comando, posicionais e nomeados, 
e imprimir ambos os argumentos posicionais e nomeados.
"""


def print_arguments_and_keyarguments(*args, **kwargs):
    print('Positional:')
    if len(args) == 0:
        print('(none)')
    for arg in args:
        print(arg)
    print('Keyword:')
    if len(kwargs) == 0:
        print('(none)')
    for key, value in kwargs.items():
        print(f'{key}:{value}')


def tests_5_14():

    print(f'Test 1.\n{"-="*30}')
    print_arguments_and_keyarguments(1, 2)

    print(f'\nTest 2.\n{"-="*30}')
    print_arguments_and_keyarguments(a=1, b=2)

    print(f'\nTest 3.\n{"-="*30}')
    print_arguments_and_keyarguments(3, 4, d=5, c=3)


if __name__ == "__main__":
    tests_5_14()
