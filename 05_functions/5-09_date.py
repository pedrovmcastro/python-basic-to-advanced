"""
Exercise 9:
Create a function that receives the current date (day, month, and year as integers) and displays it on the screen in full textual format.
Example: Date: 01/01/2000, print: January 1, 2000.


(PT-BR)
Exercício 9:
Faça uma função que receba a data atual (dia, mês e ano em inteiro) e exiba-a na tela no formato textual por extenso
Exemplo: Data: 01/01/2000, imprimir: 1 de janeiro de 2000.
"""


def main():
    # Input example: 01/01/2000
    input_date = input("Enter the date (DD/MM/YYYY): ")

    # Split the input into a list: ['01', '01', '2000']
    date_parts = input_date.split('/')
    day, month, year = int(date_parts[0]), int(date_parts[1]), int(date_parts[2])

    # Print the date in full textual format
    print(date_to_text(day, month, year))


def date_to_text(day, month, year):
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    month = months[month - 1]
    return f'{month} {day}, {year}'


if __name__ == "__main__":
    main()

