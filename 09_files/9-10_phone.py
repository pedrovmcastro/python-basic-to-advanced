"""
Exercise 10:
Create a program that allows the user to enter various names and phone numbers for registration, and generate 
a file with this informations, one per line. The user concludes the input entering "0" for phone number.

(PT-BR)
Exercício 10:
Faça um programa que permita que o usuário entre com diversos nomes e telefone para cadastro, e crie um arquivo com essas 
informações, uma por linha. O usuário finaliza a entrada com '0' para o telefone.
"""
phone_book = {}

while True:
    name = input('Name: ')
    phone_number = input('Phone number (0 to exit): ')
    if phone_number == '0':
        break
    phone_book[name] = phone_number

with open('new_text.txt', 'w') as file:
    for name, phone_number in phone_book.items():
        file.write(f'{name.title()}: {phone_number}\n')
        