"""
Exercise:

(PT-BR)
Exercício:

"""
"""
Faça uma função que receba 3 números inteiros como parâmetro, representando horas,
minutos e segundos, e os converta em segundos.
"""


def conversao_segundos(horas, minutos, segundos):
    return f'{horas*3600 + minutos*60 + segundos} segundos'


print(conversao_segundos(int(input()), int(input()), int(input())))
