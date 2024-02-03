"""
Exercise 8:
Write a program that receives the name of an input file and another for output. The input file contains, in each line, 
the name of a city and its population number. The program should read the input file and generate
an output file that contains the name of the most populous city followed by its population number.

(PT-BR)
Exercício 8:
Faça um programa que receba o nome de um arquivo de entrada e outro de saída. O arquivo de entrada contém em cada linha
o nome de uma cidade e o seu número de habitantes. O programa deverá ler o arquivo de entrada
e gerar um arquivo de saída em que aparece o nome da cidade mais populosa seguida pelo seu número de habitantes.
"""

with open('cities.txt') as file:
    text = file.readlines()

most = 0
for line in text:
    line = line.split(' ')
    hab = int(line[-1])
    if hab > most:
        most = hab
        line.pop()
        city = ' '.join(line)

with open('new_text.txt', 'w') as file:
    file.write(f'{city}: {most}')
    