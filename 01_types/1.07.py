"""
Exercise 7:
Read a temperature in Fahrenheit and display it on the screen converted to Celsius.
The conversion formula is: C = 5.0*(F - 32.0)/9.0, where C is the temperature in Celsius
and F the temperature in Fahrenheit. 

(PT-BR)
Exercício 7:
Leia uma temperatura em Graus Fahrenheit e apresenta-a convertida em graus Celsius.
A formúla de conversão é C = 5.0*(F - 32.0)/9.0, sendo C a temperatura em Celsius e F
a temperatura em Fahrenheit.
"""

F = float(input("Enter a temperature in Fahrenheit: "))

C = 5*(F - 32)/9

print(C)
