"""
Exercise 5:
Implement a program that prompts the user for the height and gender of a person (M/F), and calculates and displays on the screen their ideal weight,
considering the following formulas (where h corresponds the height):
    - Man: (72.7 * h) - 58
    - Woman: (62.1 * h) - 44.7


Exercício 5 (PT-BR):
Faça um programa que receba a altura e o sexo de uma pessoa (M/F) e calcule e mostre seu peso ideal,
utilizando as seguintes fórmulas (onde h corresponde à altura):
    - Homens: (72.7 * h) - 58
    - Mulheres: (62.1 * h) - 44.7
"""

height = float(input("Enter the height: "))
gender = input("Enter the gender (M/F): ").upper() # case-insensitive

match gender:
    case "M":
        print(f"The ideal weight is {((72.7 * height) - 58):.2f}.") 
    case "F":
        print(f"The ideal weight is {((62.1 * height) - 44.7):.2f}.") 
    case _:
        print("Gender invalid.")
