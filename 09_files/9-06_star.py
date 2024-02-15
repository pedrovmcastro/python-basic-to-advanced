"""
Exercise 6:
Write a program that receives a text file from the user. The program should creates another text file containing the 
the text from the input file, but with the vowels replaced by "*". 

(PT-BR)
Exercício 6:
Faça um programa que receba do usuário um arquivo texto. Crie outro arquivo texto contendo o texto do arquivo de 
entrada, mas com as vogais substituídas por '*'.
"""

file_name = input('Enter the file name: ')

with open(file_name) as file:
    text = file.read()

with open('new_text.txt', 'w') as file:
    for char in text:
        if char in 'aeiouAEIOU':
            file.write('*')
        else:
            file.write(char)
