"""
Exercise 1:
Write a programam that:
(a) Creates/opens a text file named "introduction.txt";
(b) Allows the user to record various characteres in this file until the user enters the character '0';
(c) Closes the file.


(PT-BR)
Exercício 1:
Escreva um programa que:
(a) Crie/abra um arquivo texto de nome "introduction.txt"
(b) Permita que o usuário grave diversos caracteres nesse arquivo, até que o usuário entre com o caractere '0'
(c) Feche o arquivo
"""

with open('introduction.txt', 'w') as file:   # "with" automatically closes the file. 
    while True:
        char = input()
        if char != '0':
            file.write(char)
        else:
            break
