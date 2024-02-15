"""
Exercise 11:
Given a file containing a set of names and birthdates (DD/MM/AAAA), create a program that reads the file name and today's
date and generates another file containing the name and age of each person from the first file.

(PT-BR)
Exercício 11:
Dado um arquivo contendo um conjunto de nome e data de nascimento (DD/MM/AAAA), faça um programa que leia o nome do arquivo
e a data de hoje e construa outro arquivo contendo o nome e a idade de cada pessoa do primeiro arquivo. 
"""

file_name = input('Enter the file name: ')
today = input("Enter today's date (DD/MM/AAAA): ")
today = today.split('/')
today_day, today_month, today_year = int(today[0]), int(today[1]), int(today[2]) 

ages = {}

with open(file_name) as file:
    text = file.readlines()

for line in text:
    line = line.split()
    
    # Age calculation:   
    date = line[-1]
    date = date.split('/')
    day, month, year = int(date[0]), int(date[1]), int(date[2])
    if month > today_month:
        age = today_year - year - 1
    else:
        if day > today_day:
            age = today_year - year - 1
        else:
            age = today_year - year
        
    line.pop()
    name = ' '.join(line)
    ages[name] = age

with open('new_text.txt', 'w') as file:
    for name, age in ages.items():
        file.write(f'{name}: {age} years old.\n')
