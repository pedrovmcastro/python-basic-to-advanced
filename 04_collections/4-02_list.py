"""
Exercise 2:
Create a program that reads 6 integer values and then displays them on the screen.

(PT-BR)
Exercício 2:
Crie um programa que lê 6 valores inteiros e, em seguida, mostre
na tela os valores lidos.
"""
lista = []

for i in range(6):
    num = int(input())
    lista.append(num)

for value in lista:
    print(value)
