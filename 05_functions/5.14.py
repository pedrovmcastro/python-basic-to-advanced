"""Resolva as sequintes questões envolvendo duas strings (str1 e str2):
a) calcula o comprimento de cada string;
b) compara as duas e retorna se são iguais ou diferentes;
c) concatena str2 em str1;
d) a funcao concatena n caracteres de str2 em str1;
e) recebe dado caractere qualquer e retorna a string com dado caractere sempre em maiúsculo.
"""


def tamanho(string):
    return len(string)


def compara(string1, string2):
    if string1 == string2:
        return 'iguais'
    else:
        return 'diferentes'


def concatena(string1, string2):
    return string1 + string2


def concatena_char(string1, string2):
    n = int(input('posicao: '))
    return string1 + string2[:n+1]


def char_maiusculo(string1, string2):

    string1_mod, string2_mod = '', ''
    char = input('caractere: ')

    for letra in string1:
        if letra == char:
            string1_mod += letra.upper()
        else:
            string1_mod += letra

    for letra in string2:
        if letra == char:
            string2_mod += letra.upper()
        else:
            string2_mod += letra

    return string1_mod, string2_mod


def main():
    str1 = input('string 1: ')
    str2 = input('string 2: ')

    op = ''

    print('\n' + '=-' * 60)

    while op != '0':
        print('Escolha uma opção')
        print(""""
        1) calcula o comprimento de cada string;
        2) compara as duas e retorna se são iguais ou diferentes;
        3) concatena str2 em str1;
        4) a funcao concatena n caracteres de str2 em str1;
        5) recebe dado caractere qualquer e retorna a string com dado caractere sempre em maiúsculo.
        """)
        op = input('1/2/3/4/5 ou 0 para sair: \n')

        if op == '0':
            break
        elif op == '1':
            print(f'Tamanho da string 1: {tamanho(str1)}\nTamanho da string 2: {tamanho(str2)}')
        elif op == '2':
            print(compara(str1, str2))
        elif op == '3':
            print(concatena(str1, str2))
        elif op == '4':
            print(concatena_char(str1, str2))
        elif op == '5':
            str1, str2 = char_maiusculo(str1, str2)
            print(str1, str2)
        print('\n' + '=-' * 60)



main()
