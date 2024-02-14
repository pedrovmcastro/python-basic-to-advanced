"""
Exercise 6:
Using match, implement a program that prompts the user for an integer between 1 and 7 and prints the corresponding 
day of the week. That is, Sunday if 1, Monday if 2, and so on.

Exercício 6 (PT-BR):
Usando match, escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana
correspondente a este número. Isto é, domingo se 1, segunda-feira se 2, e assim por diante.
"""

num = int(input("Enter an integer: "))

match num:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("Wednesday")
    case 5:
        print("Thursday")
    case 6:
        print("Friday")
    case 7:
        print("Saturday")
    case _:
        print("Invalid number")
