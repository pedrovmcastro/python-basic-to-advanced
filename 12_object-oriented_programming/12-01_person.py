"""
Exercício 1:
Escreva um código que apresente a classe Pessoa, com atributos nome, endereço e telefone e,
o método imprimir. O método imprimir deve mostrar na tela os valores de todos os atributos.
"""

class Person:
    
    def __init__(self, name, adress, phone):
        self.__name = name
        self.__adress = adress
        self.__phone = phone

    def print_object(self):
        print(f"Name: {self.__name}")
        print(f"Adress: {self.__adress}")
        print(f"Phone Number: {self.__phone}")


Tom = Person("Tom", "New York", "9817239")

Tom.print_object()
