"""
Exercise 11:
Resolve the following questions involving two strings (str1 and str2):
a) calculates the length of each string;
b) compares the two and returns whether they are equal or different;
c) concatenates str2 to str1;
d) the function concatenates n characters from str2 to str1;
e) receives any character and returns the string with the given character always in uppercase.


(PT-BR)
Exercício 11:
Resolva as sequintes questões envolvendo duas strings (str1 e str2):
a) calcula o comprimento de cada string;
b) compara as duas e retorna se são iguais ou diferentes;
c) concatena str2 em str1;
d) a funcao concatena n caracteres de str2 em str1;
e) recebe dado caractere qualquer e retorna a string com dado caractere sempre em maiúsculo.
"""


def main():
    str1 = input('String 1: ')
    str2 = input('String 2: ')

    choice = ''

    print('\n' + '=-' * 60)

    while choice != '0':
        print('Choose an option:')
        print(""""
        1) Calculate the length of each string;
        2) Compare the two and return whether they are equal or different;
        3) Concatenate str2 to str1;
        4) The function concatenates n characters from str2 to str1;
        5) Receive any character and return the string with the given character always in uppercase.
        """)
        choice = input('1/2/3/4/5 or 0 to exit: \n')

        match choice:
            case "0":
                break
            case "1":
                print(f'Length of string 1: {length(str1)}\nLength of string 2: {length(str2)}')
            case "2":
                print(compare(str1, str2))
            case "3":
                print(concatenate(str1, str2))
            case "4":
                print(concatenate_n_chars(str1, str2))
            case "5":
                str1, str2 = char_to_upper(str1, str2)
                print(str1, str2)
            
        print('\n' + '=-' * 60)


def length(string):
    return len(string)


def compare(string1, string2):
    if string1 == string2:
        return 'Equal'
    else:
        return 'Different'


def concatenate(string1, string2):
    return string1 + string2


def concatenate_n_chars(string1, string2):
    n = int(input('Position: '))
    return string1 + string2[:n+1]


def char_to_upper(string1, string2):
    string1_mod, string2_mod = '', ''
    char = input('Character: ')

    for letter in string1:
        if letter == char:
            string1_mod += letter.upper()
        else:
            string1_mod += letter

    for letter in string2:
        if letter == char:
            string2_mod += letter.upper()
        else:
            string2_mod += letter

    return string1_mod, string2_mod


if __name__ == "__main__":
    main()
