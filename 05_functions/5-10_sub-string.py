"""
Exercise 10:
Implement a function that returns the first position of a sub-string within a string.
If the sub-string is not found, the function should return -1.


(PT-BR)
Exercício 10:
Escreva uma função que retorne a primeira posição de uma sub-string dentro de uma string. Caso
a sub-string não seja encontrada, a função deve retornar -1.
"""


def main():

    st = input()
    sub_st = input()

    pos = pos_sub(st, sub_st)

    if pos != -1:
        print(pos)
    else:
        print('Do not contain the sub-string')


def pos_sub(string, sub_string):
    if sub_string in string:
        return string.index(sub_string)
    else:
        return -1


if __name__ == "__main__":
    main()
