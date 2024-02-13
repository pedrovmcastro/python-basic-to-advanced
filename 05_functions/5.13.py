"""
Exercise:

(PT-BR)
Exercício:

"""
"""
Escreva uma função que compare e retorne verdadeiro, caso uma string seja anagrama da outra, e
falso, caso contrario.
"""


def anagrama(string1, string2):
    # Verifica se são do mesmo tamanho:
    if len(string1) != len(string2):
        return False

    # Retira os espaços em branco (os substituindo por "", que é o mesmo que remover):
    string1 = string1.replace(" ", "").lower()
    string2 = string2.replace(" ", "").lower()

    """Verifica se todos os caracteres de uma string está em outra:
    for char in string1:
        if char in string2:
            string2 = list(string2)
            string2.remove(char)
            string2 = str(string2)
        else:
            return False
    """

    # No entanto, há um jeito mais simples:
    return sorted(string1) == sorted(string2)


def main():
    str1, str2 = input(), input()
    print(anagrama(str1, str2))


main()
