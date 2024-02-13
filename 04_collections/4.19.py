"""
Exercise:

(PT-BR)
Exercício:

"""
"""Faça um programa que leia dez conjuntos de dois valores, o primeiro representando
o número do aluno e o segundo representando a sua altura em metros. Encontre o aluno mais baixo
e o mais alto. Mostre o número do aluno miais baixo e do mais alto, juntamente com suas alturas"""

dicionario = {}

for _ in range(10):
    numero_aluno = int(input('Número do aluno: '))
    altura_aluno = float(input('Altura do aluno: '))
    dicionario[numero_aluno] = altura_aluno

for numero, altura in dicionario.items():
    if altura == max(dicionario.values()):
        mais_alto = numero
    if altura == min(dicionario.values()):
        mais_baixo = numero

print(f'Numero do aluno mais alto = {mais_alto}\nAltura = {max(dicionario.values())}')
print(f'Numero do aluno mais baixo = {mais_baixo}\nAltura = {min(dicionario.values())}')
