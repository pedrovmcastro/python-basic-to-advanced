"""
Exercise 4:
Write a program that receives a text file and a character from the user. Display on the screen how many times that
character occurs within the file. 

(PT-BR)
Exercício 4:
Faça um programa que receba do usuário um arquivo texto e um caractere. Mostre na tela quantas vezes aquele
caractere ocorre dentro do arquivo.
"""

file_name = input('Enter the file name: ')
char = input('Enter the character: ')
count = 0

with open(file_name) as file:
    text = file.read()
    for c in text:
        if c == char:
            count += 1

print(count)
