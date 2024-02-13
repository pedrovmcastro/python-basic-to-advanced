"""
Exercise:

(PT-BR)
Exercício:

"""
"""Escreva uma função que receba um número inteiro maior do que zero e retorne a soma de todos os seus algorismos.
Por exemplo, ao número 251 corresponderá o valor 8(2+5+1). Se o número lido não for maior do que zero, o programa
terminará com a mensagem "Número inválido"."""


def soma_algorismos(num):
    if int(num) <= 0:
        return 'Número inválido'
    algorismos = list(num)
    soma = 0
    for algorismo in algorismos:
        soma += int(algorismo)
    return soma


print(soma_algorismos(input()))
