# Exercise 5:
# Create a dictionary with some keys and values.
# Ask the user for a key to search in the dictionary.
# Try to access the key and print the corresponding value. If the key does not exist, print a message indicating it.

# (PT-BR)
# Exercício 5:
# Crie um dicionário com algumas chaves e valores.
# Solicite ao usuário uma chave para buscar no dicionário.
# Tente acessar a chave e imprimir o valor correspondente. Se a chave não existir, imprima uma mensagem indicando isso.


def search_key(dic, key):
    try:
        return f'Nota: {dic[key]}'
    except KeyError:
        return 'Nome nao esta no dicionario'


grades = {'Joao': 10, 'Maria': 9, 'Josefa': 9.5, 'Juvenal': 7.5}
key = input('Which name do you want to look up in the dictionary?')

print(search_key(grades, key))
