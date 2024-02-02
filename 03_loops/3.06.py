"""
Faça um programa que leia 10 inteiros e imprima sua media.
"""

soma = 0
for i in range(10):
    num = int(input())
    soma += num

media = soma/10
print(media)
