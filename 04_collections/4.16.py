"""
Exercise:

(PT-BR)
Exercício:

"""
"""Faça um programa para gerar automaticamente números entre 0 e 99 de uma cartela de bingo. Sabendo que
cada cartela deverá conter 5 linhas de 5 números, gere estes dados de modo a não ter números repetidos dentro das
cartelas. O programa deve exibir na tela a cartela gerada"""

import random

conjunto_bingo = set()
while len(conjunto_bingo) < 25:
    conjunto_bingo.add(random.randint(0, 99))

lista_bingo = list(conjunto_bingo)
random.shuffle(lista_bingo)

matriz_bingo = []
k = 0
for _ in range(5):
    linha = []
    for _ in range(5):
        linha.append(lista_bingo[k])
        k += 1
    matriz_bingo.append(linha)

for i in range(5):
    for j in range(5):
        print(f'[{matriz_bingo[i][j]:^5}]', end='')
    print()

"""
import random

def gerar_cartela():
    cartela = []
    for _ in range(5):
        linha = []
        while len(linha) < 5:
            numero = random.randint(0, 99)
            if numero not in linha:
                linha.append(numero)
        linha.sort()
        cartela.append(linha)
    return cartela

def exibir_cartela(cartela):
    for linha in cartela:
        print(linha)

cartela = gerar_cartela()
exibir_cartela(cartela)
"""
