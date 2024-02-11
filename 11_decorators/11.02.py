# 2). Implemente uma função chamada filtro que aceita uma função de filtro e uma lista,
# e retorna uma lista apenas com os elementos que satisfazem a condição da função de filtro.

def filtro(funcao, lista):
    return filter(funcao, lista)

def filtro_par(num):
    return num % 2 == 0

print(list(filtro(filtro_par, [1, 2, 3, 4, 5, 6, 7])))

# Alternative way:
print(list(filtro(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6, 7])))
