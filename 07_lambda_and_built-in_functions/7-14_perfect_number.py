# Exercise 14:
# Write a function that uses filter() to return a list with numbers that are perfect from a given list.
# A number is perfect if the sum of its proper divisors (excluding itself) is equal to the number.
# For example, 6 is perfect because 6 = 1 + 2 + 3. If the list is [6, 12, 28, 30], the function should return [6, 28].

# (PT-BR)
# Exercício 14:
# Escreva uma função que use filter() para retornar uma lista com os números que são perfeitos de uma lista dada. 
# Um número é perfeito se a soma dos seus divisores próprios (excluindo ele mesmo) é igual a ele. 
# Por exemplo, 6 é perfeito porque 6 = 1 + 2 + 3. Se a lista for [6, 12, 28, 30], a função deve retornar [6, 28].

lista = [6, 12, 28, 30]


def divisors(num):
    return [x for x in range(1, num//2 + 1) if num % x == 0]


print(list(filter(lambda x: sum(divisors(x)) == x, lista)))

# With List Comprehension:
print([num for num in lista if sum(divisors(num)) == num])
