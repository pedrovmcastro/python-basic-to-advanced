"""
Exercise 5:
Create a function that receives 3 integer numbers as parameters, representing hours, minutes and seconds,
and converts them to seconds.

(PT-BR)
Exercício 5:
Faça uma função que receba 3 números inteiros como parâmetro, representando horas,
minutos e segundos, e os converta em segundos.
"""


def convert_to_seconds(hours, minutes, seconds):
    return f'{hours*3600 + minutes*60 + seconds} seconds'



print(convert_to_seconds(int(input("First: ")), int(input("Second: ")), int(input("Third: "))))
