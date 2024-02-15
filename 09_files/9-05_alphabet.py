"""
Exercise 5:
Write a program that receives a text file from the user and displays on the screen how many times each letter of the alphabet
occurs within the file. 

(PT-BR)
Exercício 5:
Faça um programa que receba do usuário um arquivo texto e mostre na tela quantas vezes cada letra do alfabeto aparece
dentro do arquivo.
"""

file_name = input("Enter the file name: ")
alphabet = 'abcedefghijklmnopqrstuvwxyz'

with open(file_name) as file:
    text = file.read()

count_letters = []
for i in range(26):
    count = 0
    for char in text:
        if char.lower() == alphabet[i]:
            count += 1
    count_letters.append(count)

for i in range(26):
    print(f'Letter {alphabet[i]}: {count_letters[i]}')
    