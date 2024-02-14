"""
Exercise 1:
Implement a program that takes two numbers as input and shows which one is greater.

Exercício 1 (PT-BR):
Faça um programa que receba dois números e mostre qual deles é o maior.
"""

print("Enter two numbers (one per line):")
n1, n2 = int(input()), int(input())

if n1 > n2:
    print(f"{n1} is greater.")
elif n1 < n2:
    print(f"{n2} is greater.")
else:
    print("Both numbers are the same.")
