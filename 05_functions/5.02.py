"""
Faça uma função que receba a data atual (dia, mês e ano em inteiro) e exiba-a na tela no formato textual por extenso
Exemplo: Data: 01/01/2000, imprimir: 1 de janeiro de 2000.
"""


def data_extenso(dia, mes, ano):
    return f'{dia} de {mes} de {ano}'


# Cria uma lista a partir da entrada do usuário, identificando '/' como separador entre os elementos:
# '01/01/2000' -> ['01', '01', '2000']
data = input().split('/')

# Atribuição de cada elemento da lista - dia, mês e ano:
dia, mes, ano = int(data[0]), int(data[1]), int(data[2])

# Cria uma lista com os meses:
meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro',
         'novembro', 'dezembro']
mes = meses[mes-1]

print(data_extenso(dia, mes, ano))
