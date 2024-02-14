"""
Exercise 4:
Create a program that reads 10 integers and prints their mean.

(PT-BR)
Exercício 4
Faça um programa que leia 10 inteiros e imprima sua media.
"""

sum = 0
for i in range(10):
    n = int(input("Enter a value: "))
    sum += n

mean = sum/10
print(mean)
