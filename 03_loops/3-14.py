"""
Exercise 14:
Create a program that receives an integer greater than 1 and checks whether the provided number is prime or not.

(PT-BR)
Exercício 14:
Faça um prorgama que recebe um inteiro maior do que 1 e checa se o número é primo ou não.
"""
import math

num = int(input("Enter a number: "))

if num <= 1: 
    print("Must be greater than 1")
else:
    is_prime = True
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print("The number is prime.")
else:
    print("The number is not prime.")
    