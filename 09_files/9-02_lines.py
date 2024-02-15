"""
Exercise 2:
Write a program that receives a text file from the user and displays on the screen how many lines this file has.

(PT-BR)
Exercício 2:
Faca um programa que receba do usuario um arquivo texto e mostre na tela quantas linhas esse arquivo possui.
"""

file_name = input("What's the name of the file? ")
count = 0

with open(file_name) as file:
    for linha in file:
        count += 1

print(count)
