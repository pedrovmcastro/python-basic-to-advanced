"""
Exercise 7:
Create a function that receives two positive integers as parameters and returns the sum of the integers existing between them.


(PT-BR)
Exercício 7:
Faça uma função que receba dois números inteiros positivos por parâmetro e retorne a soma dos N números
inteiros existentes entre eles.
"""


def sum_between_numbers(num1, num2):
    if num1 <= 0 or num2 <= 0:
        return 'Invalid values'
    elif num2 < num1:
        tmp = num1
        num1 = num2
        num2 = tmp
    total_sum = 0
    for num in range(num1 + 1, num2):
        total_sum += num
    return total_sum


print(sum_between_numbers(int(input("Enter the first number: ")), int(input("Enter the second number: "))))
