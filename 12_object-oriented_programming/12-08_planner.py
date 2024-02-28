"""
Exercise 8:

Create a class Planner that can store information for 10 people and is capable of performing the following operations:

    store_person(name, age, height)
    remove_person(name)
    search_person(name) - informs the position of the person in the planner
    print_planner() - prints the data of all people in the planner
    print_person(index) - prints the data of the person at the specified index


(PT-BR)
Exercício 8:
Crie uma classe Agenda que pode armazenar 10 pessoas e seja capaz de realizar as seguintes operações:
    > armazena_pessoas(nome, idade, altura)
    > remove_pessoa(nome)
    > busca_pessoa(nome) - informa em que posição da agenda está a pessoa
    > imprime_agenda() - imprime os dados de todas as pessoas da agenda
    > imprime_pessoa(indice) - imprime os dados da pessoa que está na posição do índice
"""

class Planner:

    def __init__(self):
        self.__people = []

    def store_person(self, name, age, height):
        if len(self.__people) < 10:
            person = {'name': name, 'age': age, 'height': height}
            self.__people.append(person)
            print(f'{name} has been added to the planner')
        else:
            print('Planner full. Unable to add more people')

    def remove_person(self, name):
        for contact in self.__people:
            if contact['name'] == name:
                self.__people.remove(contact)
                print(f'{name} has been removed from the planner')
                return 
        print(f'{name} is not in the planner')

    def search_person(self, name):
        for i, contact in enumerate(self.__people, 1):
            if contact['name'] == name:
                print(f'{name} is at position {i} in the planner')
                return
        print(f'{name} is not in the planner')

    def print_planner(self):
        for contact in self.__people:
            print(f'Name: {contact["name"]}, Age: {contact["age"]}, Height: {contact["height"]}')

    def print_person(self, index):
        if 1 <= index <= 10:
            print(f'Name: {self.__people[index]["name"]}, Age: {self.__people[index]["age"]}, Height: {self.__people[index]["height"]}')
            return
        print('Invalid index')


# Creating the planner object:
planner = Planner()

# Adding people:
planner.store_person('Pedro', 33, 1.78)
planner.store_person('Rebeca', 23, 1.56)
planner.store_person('Luis', 29, 1.77)
planner.store_person('Cris', 63, 1.61)
planner.store_person('Juarez', 59, 1.8)

# Removing a person:
planner.remove_person('Juarez')

# Searching for a person:
planner.search_person('Cris')

# Printing the planner:
planner.print_planner()

# Printing a person:
planner.print_person(2)