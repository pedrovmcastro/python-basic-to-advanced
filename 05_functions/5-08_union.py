"""
Exercise 8:
Create a function that receives, as parameters, two arrays of 10 integer elements each and calculates and returns,
also as a parameter, the union array of the first two.


(PT-BR)
Exercício 8:
Faça uma função que recebe, por parâmetro, 2 vetores de 10 elementos inteiros e que calcule e retorne, também
por parâmetro, o vetor união dos dois primeiros.
"""


def main():
    arr1 = [0, 1, 2, 4, 5, 6, 2, 0, 1, 7]
    arr2 = [8, 1, 3, 6, 9, 10, 13, 6, 6, 1]
    print(union_arrays(arr1, arr2))


def union_arrays(arr1, arr2):
    return list(set(arr1 + arr2))
    

if __name__ == "__main__":      # Using this you can import your custom function without call the main function.
    main()
    