"""
Exercise 9:
Create a program that receives from the user two arrays, A and B, each with 10 integer numbers. 
Create an array named C by calculating C = A - B. Display the data of array C on the screen.

(PT-BR)
Exercício 9:
Faça um programa que receba do usuário dois vetores, A e B, com 10 números inteiros cada.
Crie um vetor denominado C calculando C = A - B. Mostre na tela os dados do vetor C
"""

A, B, C = [], [], []

print('Enter the values for array A:')
for _ in range(10):
    A.append(int(input()))

print('Enter the values for array B:')
for _ in range(10):
    B.append(int(input()))

for value in A:
    if value in A and value not in B:
        C.append(value)

print(C, end='')
