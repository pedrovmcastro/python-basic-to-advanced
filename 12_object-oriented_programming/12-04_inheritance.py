"""
Exercício 4: 
Crie um novo pacote com o nome: herança. Todas as (três) classes criadas abaixo deverão ser salvas nesse pacote.

a) Crei uma classe Equipamento com dois atributos privados.

b) Crie uma classe Computador com dois atributos à sua escolha, também privados.
A classe Computador deverá herdar tudo da classe Equipamento. 

c) Crie os métodos de acesso e modificação para todos os atributos definidos em ambas as classes.

d) Crie uma classe TestaEquipamento, que deverá conter o método main(), crie nela um objeto da classe 
Equipamento e instancie os dois atributos que você declarou na classe Equipamento. Crie também um objeto
da classe Computador, utilizando os atributos declarados na própria classe e os dois herdados da classe Equipamento.

e) O método main() deve exibir as informações dos dois objetos criados. 

f) Criar o método exibe() na classe Equipamento para mostrar os dados dessa classe.

g) Reescreva o método exibe() na classe Computador, aproveitando o que já está escrito na superclasse Equipamento.
"""

class Equipment:

    def __init__(self, name, voltage):
        self.__name = name
        self.__voltage = voltage
        self.__on = False

    @property
    def name(self):
        return self.__name
    
    @property
    def voltage(self):
        return self.__voltage
    
    @property
    def is_on(self):
        return self.__on
    
    def display(self):
        return f"Equipment: {self.__name}\nVoltage: {self.__voltage}\n"


class Computer(Equipment):

    def __init__(self, name, voltage, brand, RAM):
        super().__init__(name, voltage)
        self.__brand = brand
        self.__RAM = RAM

    @property
    def brand(self):
        return self.__brand
    
    @property
    def RAM(self):
        return self.__RAM
    
    def display(self):
        print(super().display(), end="")
        return f"Brand: {self.__brand}\nRAM: {self.__RAM}\n"
    

class EquipmentTest:

        @classmethod
        def main(cls):
            equip1 = Equipment("Laptop", "110V")
            computer1 = Computer("Laptop", "110V", "Lenovo", "8GB")
            print(f"Equipment: {equip1.name}\nVoltage: {equip1.voltage}\n")
            print(f"Equipment: {computer1.name}\nVoltage: {computer1.voltage}\nBrand: {computer1.brand}\nRAM: {computer1.RAM}\n")
            
print("TEST 1")
EquipmentTest.main()

print("TEST 2")
equip2 = Equipment("Desktop", "110V")
print(equip2.display())

print("TEST 3")
computer2 = Computer("Desktop", "110V", "Apple", "16GB")
print(computer2.display(), end="")
print(computer2.is_on)
