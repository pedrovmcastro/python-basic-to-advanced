"""
Exercise 9:
Open a text file and display on the screen the number of characters, number of lines and number of words in this file.

(PT-BR)
Exercício 9:
Abra um arquivo texto, calcule e escreva o número de caracteres, o número de linhas e o número de palavras neste arquivo.
"""

lines, words, characters = 0, 0, 0

with open('file_name.txt') as file:
    text = file.read()
    file.seek(0)    # To return to the initial position in the file.
    for line in file:
        lines += 1
    
words = len(text.split())

for char in text:
    characters += 1

print(f'Lines = {lines}; Words = {words}; Characters = {characters}')
