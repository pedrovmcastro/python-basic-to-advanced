"""
Exercise 17:
Read two arrays of integers, x and y, each with 5 elements (assume that the user does not input repeated elements).
Calculate and display the resulting arrays in each of the following cases:
    -> Sum between x and y: sum of each element in x with the element at the same position in y;
    -> Product between x and y: multiplication of each element in x with the element at the same position in y;
    -> Difference between x and y: all elements in x that do not exist in y;
    -> Intersection between x and y: only the elements that appear in both arrays;
    -> Union between x and y: all elements in x, and all elements in y that are not in x.

    
(PT-BR)
Exercício 17:
Leia dois vetores de inteiros x e y, cada um com 5 elementos(assuma que o usuário não informa
elementos repetidos). Calcule e mostre os vetores resultantes em cada caso abaixo:
    -> Soma entre x e y: soma de cada elemento de x com o elemento da mesma posição em y;
    -> Produto entre x e y: multiplicação de cada elemento de x com o elemento da mesma posição em y;
    -> Diferença entre x e y: todos os elementos de x que não existem em y;
    -> Intersecção entre x e y: apenas os elementos que aparecem nos dois vetores;
    -> União entre x e y: todos os elementos de x, e todos os elementos de y que não estão em x.
"""

def read_arr():
    arr = []
    for _ in range(5):
        arr.append(int(input()))
    return arr

x = read_arr()
y = read_arr()

sum_arr, product_arr, difference_arr, intersection_arr, union_arr = [], [], [], [], []

for i, value in enumerate(x):
    sum_arr.append(x[i] + y[i])
    product_arr.append(x[i] * y[i])

difference_arr = set(x).difference(y)
intersection_arr = set(x).intersection(y)
union_arr = set(x).union(y)

print('Vector x = ', x)
print('Vector y = ', y)
print('Sum vector = ', sum_arr)
print('Product vector = ', product_arr)
print('Difference vector = ', list(difference_arr))
print('Intersection vector = ', list(intersection_arr))
print('Union vector = ', list(union_arr))
