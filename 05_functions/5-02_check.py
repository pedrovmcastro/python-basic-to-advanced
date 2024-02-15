"""
Exercise 2:
Create a function to checks whether a number is positive or negative.  
The return value should be 1 if positive, -1 if negative, and 0 if it is equal to 0.

(PT-BR)
Exercício 2:
Faça uma função para verificar se um número é positivo ou negativo. Sendo que o valor de retorno será 1 se positivo,
-1 se negativo e 0 se for igual a 0.
"""


def check_num(num):
    if num > 0:
        return 1
    elif num < 0:
        return -1
    else:
        return 0


print(check_num(int(input("Enter a number: "))))
