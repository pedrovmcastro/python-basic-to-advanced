"""
Exercise 6:
Write a code that defines the class Motorcycle, with attributes brand, model, color, gear, and the method print. 
The print method should display on the screen the values of all attributes. 
The gear attribute indicates the current gear of the motorcycle, represented as an integer, where 0 - neutral, 1 - first, 2 - second, etc.

Implement the following:

a) The methods shift_up and shift_down, which should change the gear. The print method should be modified to display
the values of all attributes.

b) The attributes min_gear and max_gear, indicating the lowest and highest possible gears for the motorcycle. 
The shift_up and shift_down methods should be rewritten to prevent changing gears to values below or above the possible range.

c) Add the attribute engine_on, which will indicate whether the motorcycle is turned on or off. 
This attribute should be of boolean type. Modify the print method to display the values of all attributes.

d) Add the methods turn_on and turn_off, which should change the content of the engine_on attribute accordingly.


(PT-BR)
Exercício 6: 
Escreva um código que apresente a classe Moto, com atributos marca, modelo, cor 
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
        print("On" if self.__on else "Off")


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
