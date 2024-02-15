"""
Exercise 7:
Write a program that receives two text files from the user, and cretes a third file with the content of the two files combined.

(PT-BR)
Exercício 7:
Faça um programa que receba dois arquivos do usuário, e crie um terceiro arquivo com o conteúdo dos dois primeiros juntos.
"""

file_name1 = input('Enter the first file name: ')
file_name2= input('Enter the second file name: ')

with open(file_name1) as file:
    text1 = file.read()

with open(file_name2) as file:
    text2 = file.read()

with open('new_text.txt', 'w') as file:
    file.write(text1 + text2)
    