"""
Exercise:

(PT-BR)
Exercício:

"""
"""Foi realizada uma pesquisa de algumas características fisicas de cinco habitantes de certa regiao.
De cada habitante foram coletados os seguintes dados: sexo, cor dos olhos(A - Azuis ou C - Castanhos),
cor dos cabelos(L - Louros, P - Pretos, C - Castanhos) e idade.
    - Faça uma funcao que leia esses dados em um vetor.
    - Faca uma funcao que determine a media de idade das pessoas com olhos castanhos e cabelos pretos
    - Faca uma funcao que determine e devolva ao programa principal a maior idade entre os habitantes
    - Faca uma funcao que determine e devolva ao programa princial a quantidade de indivíduos do sexo feminino
    cuja idade esta entre 18 e 35 (inclusive) e que tenham olhos azuis e cabelos louros."""

from collections import namedtuple


def read_data():
    sexo = input('Digite o sexo (M/F): ')
    eyes_color = input('Digite a cor dos olhos (A - Azuis ou C - Castanhos): ')
    hair_color = input('Digite a cor dos cabelos (L - Louros, P - Pretos, C - Castanhos): ')
    age = int(input('Digite a idade: '))

    pessoa = namedtuple('pessoa', 'sexo, eyes_color, hair_color, age')
    return pessoa(sexo=sexo, eyes_color=eyes_color, hair_color=hair_color, age=age)


def media(database):
    soma, i = 0, 0
    for pessoa in database:
        if pessoa.hair_color == 'P' and pessoa.eyes_color == 'C':
            soma += pessoa.age
            i += 1
    return soma/i


def maior_idade(database):
    maior = -1
    for pessoa in database:
        if pessoa.age > maior:
            maior = pessoa.age
    return maior


def quantidade(database):
    qtd = 0
    for pessoa in database:
        if pessoa.sexo == 'F' and pessoa.hair_color == 'L' and pessoa.eyes_color == 'A' and 18 <= pessoa.age <= 35:
            qtd += 1
    return qtd


data = []
for _ in range(5):
    data.append(read_data())

print(f'Media = {media(data)}')
print(f'Maior idade = {maior_idade(data)}')
print(f'Quantidade = {quantidade(data)}')
