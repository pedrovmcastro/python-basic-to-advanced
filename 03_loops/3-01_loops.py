"""
Exercise 1:
Implement a program that prints on the screen, from 1 to 100, in increments of 1, twice. 
The first time, use a for loop, and the second time, use a while loop.

(PT-BR)
Exercício 1:
Escreva um programa que escreva na tela, de 1 a 100, de 1 em 1, 2 vezes.
A primeira vez deve usar a estrutura de repetição for, a segunda while.
"""

for i in range(1, 101):
    print(i)
print()

i = 1
while i != 101:
    print(i)
    i += 1
