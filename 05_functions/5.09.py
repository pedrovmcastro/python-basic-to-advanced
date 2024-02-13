"""
Exercise:

(PT-BR)
Exercício:

"""
"""Faça uma função que receba dois números inteiros positivos por parâmetro e retorne a soma dos N números
inteiros existentes entre eles."""


def soma_entre_numeros(num1, num2):
    if num1 <= 0 or num2 <= 0:
        return 'valores inválidos'
    elif num2 < num1:
        tmp = num1
        num1 = num2
        num2 = tmp
    soma = 0
    for num in range(num1+1, num2):
        soma += num
    return soma


print(soma_entre_numeros(int(input()), int(input())))
