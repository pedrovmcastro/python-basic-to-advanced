"""
Exercise 10:
Read a positive number from the user, then calculate and print the Fibonacci sequence
until the first number greater than the one entered.
Example: if the user entered the number 30, 
the sequence to be printed will be 0 1 1 2 3 5 8 13 21 34


(PT-BR)
Exercício 10:
Leia um número positivo do usuário, então, calcule e imprima a
sequencia Fibonacci até o primeiro número superior ao número lido.
Exemplo: se o usuario informou o numero 30,
a sequencia a ser impresa será 0 1 1 2 3 5 8 13 21 34
"""

num = int(input("Enter a positive number: "))
a, b = 0, 1

while a <= num:
    print(a, end=" ")
    a, b = b, a + b
