"""
Exercise 3:
Write a programa that receives a text file from the user and displays on the screen how many letters are vowels.

(PT-BR)
Exercício 3:
Faça um programa que receba do usuario um arquivo texto e mostre na tela quantas letras sao vogais.
"""

file_name = input('Enter the file name: ')
vowels = 'aeiouAEIOU'
count = 0

with open(file_name, 'r') as file:
    text = file.read()
    for char in text:
        if char in vowels:
            count += 1

print(count)
