"""
Faça uma função para verificar se um número é positivo ou negativo. Sendo que o valor de retorno será 1 se positivo,
-1 se negativo e 0 se for igual a 0.
"""


def verifica_num(num):
    if num > 0:
        return 1
    elif num < 0:
        return -1
    else:
        return 0


print(verifica_num(int(input())))
