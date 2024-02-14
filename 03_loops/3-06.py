"""
Exercise 6:
Write a program that reads a positive integer N and prints all even natural numbers from 0 to N in ascending order.

(PT-BR)
Exercício 6:
Faça um programa que leia um número inteiro positivo N e imprima todos os números naturais
pares de 0 até N em ordem crescente.
"""

N = int(input("Enter a positive integer: "))

if N > 0:
    for i in range(0, N+1, 2):
        print(f"{i} ", end="")
else:
    print("Must be positive")
