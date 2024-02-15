"""
Exercise 13:
A survey was conducted on some physical characteristics of five residents of a certain region. 
The following data were collected for each resident: 
gender, eye color (A - Blue or C - Brown), hair color (L - Blond, P - Black, C - Brown), and age.
    Create a function that reads this data into an array.
    Create a function that determines the average age of people with brown eyes and black hair.
    Create a function that determines and returns to the main program the oldest age among the residents.
    Create a function that determines and returns to the main program the quantity of females whose age is between 18 and 35 (inclusive) 
    and who have blue eyes and blond hair.

    
(PT-BR)
Exercício 13:
Foi realizada uma pesquisa de algumas características fisicas de cinco habitantes de certa regiao.
De cada habitante foram coletados os seguintes dados: sexo, cor dos olhos(A - Azuis ou C - Castanhos),
cor dos cabelos(L - Louros, P - Pretos, C - Castanhos) e idade.
    - Faça uma funcao que leia esses dados em um vetor.
    - Faca uma funcao que determine a media de idade das pessoas com olhos castanhos e cabelos pretos
    - Faca uma funcao que determine e devolva ao programa principal a maior idade entre os habitantes
    - Faca uma funcao que determine e devolva ao programa princial a quantidade de indivíduos do sexo feminino
    cuja idade esta entre 18 e 35 (inclusive) e que tenham olhos azuis e cabelos louros.
    """

from collections import namedtuple
# namedtuples are like structs or classes without methods

def main():
    data = []
    
    for _ in range(5):
        data.append(read_data())

    print(f'Average Age = {average_age_brown_eyes_black_hair(data)}')
    print(f'Oldest Age = {oldest_age(data)}')
    print(f'Quantity = {quantity_females_between_18_and_35(data)}')


def read_data():
    gender = input('Enter gender (M/F): ')
    eyes_color = input('Enter eye color (A - Blue or C - Brown): ')
    hair_color = input('Enter hair color (L - Blond, P - Black, C - Brown): ')
    age = int(input('Enter age: '))

    person = namedtuple('person', 'gender, eyes_color, hair_color, age')
    return person(gender=gender, eyes_color=eyes_color, hair_color=hair_color, age=age)


def average_age_brown_eyes_black_hair(database):
    total_age, count = 0, 0
    for person in database:
        if person.hair_color == 'P' and person.eyes_color == 'C':
            total_age += person.age
            count += 1
    return total_age / count if count > 0 else 0


def oldest_age(database):
    max_age = -1
    for person in database:
        if person.age > max_age:
            max_age = person.age
    return max_age


def quantity_females_between_18_and_35(database):
    count = 0
    for person in database:
        if person.gender == 'F' and person.hair_color == 'L' and person.eyes_color == 'A' and 18 <= person.age <= 35:
            count += 1
    return count

if __name__ == "__main__":
    main()
