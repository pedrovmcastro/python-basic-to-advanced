"""
Exercise 15:
Create a function that accepts a variable number of dictionarys as named arguments (kwargs)
and merges them into a single dictionary.

(PT-BR)
Exercício 15:
Crie uma função que aceite um número variável de dicionários como argumentos nomeados
e os una em um único dicionário.
"""


def concat_dict(*args, **kwargs):
    new_dict = {}
    for dict in kwargs.values():
        for key, value in dict.items():
            new_dict[key] = value
    return new_dict


def tests_5_15():

    print(concat_dict(dic1={'a': 1, 'b': 2}, dict2={'c': 3})) # {'a': 1, 'b': 2, 'c': 3}

    print(concat_dict({'a': 1, 'b': 2}, dict1={'c': 3}, dict2={'d': 4, 'e': 5})) # Will only merge the named dictionaries

    
if __name__ == "__main__":
    tests_5_15()
