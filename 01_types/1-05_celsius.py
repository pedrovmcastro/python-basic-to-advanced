"""
Exercise 5:
Read a temperature in Celsius and display it on the screen converted to Fahrenheit.
The conversion formula is: F = C*(9.0/5.0)+32.0, where C is the temperature in Celsius
and F is the temperature converted in Fahrenheit. 

(PT-BR)
Exercício 5:
Leia uma temperatura em graus Celsius e apresente-a convertida
em Fahrenheit. A fórmula de conversão é: F = C*(9.0/5.0)+32.0,
sendo C a temperatura em Celsius e F a temperatura em Farenheit.
"""

C = float(input("Enter a temperature in Celsius: "))

F = C*(9/5) + 32

print(F)

