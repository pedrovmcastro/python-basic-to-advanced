"""
Crie um programa que lê 6 valores inteiros e, em seguida, mostre
na tela os valores lidos.
"""
lista = []

for i in range(6):
    num = int(input())
    lista.append(num)

for valor in lista:
    print(valor)
