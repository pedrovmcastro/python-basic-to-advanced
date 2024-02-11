# Exercício 18: 
# Crie uma função que aceite um número variável de dicionários como argumentos nomeados
# e os una em um único dicionário.

def concat_dict(*args, **kwargs):
    new_dict = {}
    for dict in kwargs.values():
        for key, value in dict.items():
            new_dict[key] = value
    return new_dict

print(concat_dict(dic1={'a': 1, 'b': 2}, dict2={'c': 3})) # {'a': 1, 'b': 2, 'c': 3}

# Testando:
print(concat_dict({'a': 1, 'b': 2}, dict1={'c': 3}, dict2={'d': 4, 'e': 5})) # Só unirá os dicionários nomeados
