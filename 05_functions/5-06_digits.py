"""
Exercise 6:
Write a function that receives a positive integer and returns the sum of all its digits. 
For example, the number 251 should result in the value 8 (2+5+1). 
If the provided number is not greater than zero, the program should terminate with the message 'Invalid number.


(PT-BR)
Exercício 6:
Escreva uma função que receba um número inteiro maior do que zero e retorne a soma de todos os seus algorismos.
Por exemplo, ao número 251 corresponderá o valor 8(2+5+1). Se o número lido não for maior do que zero, o programa
terminará com a mensagem "Número inválido".
"""


def sum_digits(num):
    if int(num) <= 0:
        return 'Invalid number'
    digits = list(num)
    total_sum = 0
    for digit in digits:
        total_sum += int(digit)
    return total_sum


print(sum_digits(input("Enter a positive integer: ")))
