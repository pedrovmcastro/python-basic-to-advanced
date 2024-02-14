"""
Exercise 3:
Read a set of real numbers, store them in an array, and calculate the square of the components of this array, storing the results in another array. 
Both sets have 10 elements each. Print both sets.


(PT-BR)
Exercício 3:
Ler um conjunto de números reais, armazenando-os em vetor e calcular o quadrado
das componentes deste vetor, armazenando o resultado em outro vetor.
os conjuntos têm 10 elementos cada. imprimir todos os conjuntos.
"""

set1, set2 = [], []

for i in range(10):
    N = float(input())
    set1.append(N)

for value in set1:
    value **= 2
    set2.append(value)

print(set1)
print(set2)
