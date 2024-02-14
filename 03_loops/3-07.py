"""
Exercise 7:
Implement a program that reads a positive number and prints its divisors.

(PT-BR)
Exercício 7:
Faça um algoritmo que leia um número positivo e imprima seus divisores.
"""

N = 0
while N <= 0:
    N = int(input("Enter a positive value: "))

for i in range(1, N+1):
    if N % i == 0:
        print(f"{i} ", end="")
