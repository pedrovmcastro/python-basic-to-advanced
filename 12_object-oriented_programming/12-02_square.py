"""
Exercício 2:
Escreva um código que apresente a classe Quadrado, com atributos lado, área e perímetro e,
os métodos calcular_area, calcular_perimetro e imprimir. Os métodos calcular_area e 
calcular_perimetro devem efetuar seus respectivos cálculos e colocar os valores nos atributos
area e perimetro. O método imprimir deve mostrar na tela os valores de todos os atributos.
"""

class Square:

    def __init__(self, side):
        self.__side = side
        self.__area = self.calculate_area()
        self.__perimeter = self.calculate_perimeter()

    def calculate_area(self):
        return self.__side ** 2

    def calculate_perimeter(self):
        return self.__side * 4

    def print_object(self):
        print(f"Side: {self.__side}")
        print(f"Area: {self.__area}")
        print(f"Perimeter: {self.__perimeter}")


square1 = Square(3.0)
square2 = Square(5.5)

square1.print_object()
print()
square2.print_object()
        