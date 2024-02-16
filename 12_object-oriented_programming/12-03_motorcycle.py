"""
Exercício 3: Escreva um código que apresente a classe Moto, com atributos marca, modelo, cor 
e marcha e, o método imprimir. O método imprimir deve mostrar na tela os valores de todos os
atributos. O atributo marcha indica em que marcha a Moto se encontra no momento, sendo representado
de forma inteira, onde 0 - neutro, 1 - primeira, 2 - segunda, etc. 

Faça também os seguintes implementações:

a) Os métodos marcha_acima e marcha_abaixo, que deverão efetuar a troca de marchas. O método imprimir
deve ser modificado de forma a mostrar na tela os valores de todos os atributos. 

b) Os atributos menor_marcha e maior_marcha, indicando a menor marcha possível para a moto 
e a maior marcha possível. Os métodos marcha_acima e marcha_abaixo devme ser reescritos de 
forma a não permitirem a troca de marchas para valores abaixo ou acima dos possíveis. 

c) Adicione o atributo ligada que terá a função de indicar se a moto está ligada ou não.
Esse atributo deverá ser do tipo boleano. O método imprimir deve ser modificado de forma a 
mostrar na tela os valores de todos os atributos.

d) Adicione os métodos ligar e desligar que deverão mudar o conteúdo do atributo conforme o caso.
"""

class Motorcycle:
    
    def __init__(self, brand, model, color, gear, hi_gear, low_gear):
        self.__brand = brand
        self.__model = model
        self.__color = color 
        if hi_gear < low_gear or gear not in range(low_gear, hi_gear+1) or not isinstance(gear, int) or low_gear < 0 or hi_gear > 6:
            raise ValueError("Invalid gear.")
        self.__gear = gear
        self.__hi_gear = hi_gear
        self.__low_gear = low_gear
        self.__on = False

    def turn_on(self):
        if self.__on:
            print("Already on.\n")
        self.__on = True

    def turn_off(self):
        if not self.__on:
            print("Already off.\n")
        self.__on = False

    def upshift(self):
        if self.__gear < self.__hi_gear:
            self.__gear += 1
        else:
            print("Already in the highest gear.\n")
                
    def downshift(self):
        if self.__gear > self.__low_gear:
            self.__gear += 1
        else:
            print("Already in the lowest gear.\n")
                     
    def print_object(self):
        print(f"Brand: {self.__brand}")
        print(f"Model: {self.__model}")
        print(f"Color: {self.__color}")
        print(f"Gear: {self.__gear}")
        print(f"Highest Gear: {self.__hi_gear}")
        print(f"Lowest Gear: {self.__low_gear}")
        print("Ligada" if self.__on else "Desligada")


moto1 = Motorcycle("Honda", "CB500X", "black", 0, 5, 0)
moto2 = Motorcycle("Yamaha", "MT-07", "red", 0, 4, 0)


# Tests:
moto1.print_object()
print()
moto2.print_object()
print()

moto1.turn_on()
moto1.turn_on()  # Already on.
moto2.turn_on()
moto2.turn_off()

moto1.print_object()
print()
moto2.print_object()
print()

moto1.downshift()  # Already in the lowest gear.
moto1.upshift()
moto1.upshift()
moto1.upshift()
moto1.upshift()
moto1.upshift()
moto1.upshift()  # Already in the highest gear.
moto1.print_object()
print()
