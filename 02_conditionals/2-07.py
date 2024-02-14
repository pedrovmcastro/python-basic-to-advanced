"""
Exercise 7:
Given three values, A, B, C, check if they can be the lengths of the sides of a triangle
and, if they are, determine whether the triangle is scalene, equilateral, or isosceles, considering the following concepts:
 - The length of each side of a triangle is less than the sum of the other two sides.
 - A triangle is called equilateral if it has the same length for two sides.
 - A triangle is considered scalene if all three sides have different lengths.

Exercício 7 (PT-BR):
Dados três valores, A, B, C, verificar se eles podem ser valores dos lados de um triângulo
e, se forem, se é um triângulo escaleno, equilátero ou isóscele, considerando os seguintes conceitos:
 - O comprimento de cada lado de um triângulo é menor do que a soma dos outros dois lados.
 - Chama-se equilátero o triângulo que tem o comprimento de dois lados iguais.
 - Recebe o nome de escaleno o triângulo que tem os três lados diferentes.
"""

print("Enter the values:")
A = float(input("A: "))
B = float(input("B: "))
C = float(input("C: "))

if A + B > C and A + C > B and B + C > A:
    if A == B == C:
        print("Equilateral")
    elif A != B != C:
        print("Scalene")
    else:
        print("Isosceles")
else:
    print("Not a valid triangle")
