"""
Exercise:

(PT-BR)
Exercício:

"""
"""Faça um programa que leia um numero inteiro N e depois imprima os N primeiros números naturais impaares"""

N = int(input())
cont = 0
i = 1

while cont != N:
    if i % 2 != 0:
        print(i)
        cont += 1
    i += 2
