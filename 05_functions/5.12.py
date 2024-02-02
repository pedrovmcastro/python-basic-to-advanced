"""Escreva uma função que retorne a primeira posição de uma sub-string dentro de uma string. Caso
a sub-string não seja encontrada, a função deve retornar -1."""


def main():

    st = input()
    sub_st = input()

    pos = pos_sub(st, sub_st)

    if pos != -1:
        print(pos)
    else:
        print('não contém a string')


def pos_sub(string, sub_string):
    if sub_string in string:
        return string.index(sub_string)
    else:
        return -1


main()
