"""
Exercise 4:
Create a function for calculating the volume of a sphere. 
The radius is passed as a parameter.
V = 4/3*pi*R³

(PT-BR)
Exercício 4:
Faça uma função para o cálculo do volume de uma esfera.
Sendo que o raio é passado por parâmetro.
V = 4/3*pi*R³
"""

from math import pi


def sphere_volume(radius):
    return (4/3)*pi*radius**3


print(sphere_volume(int(input("Enter the radius: "))))
