"""
Exercise:

(PT-BR)
Exercício:

"""
"""Faça um programa que leia 10 numeros inteiros positivos, ignorando não positivos, e imprima sua media"""

soma = 0
for i in range(10):
    num = int(input())
    if num > 0:
        soma += num

media = soma/10
print(media)
        