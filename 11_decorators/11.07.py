# 7). Desenvolva uma função de alta ordem chamada filtro_composto que aceita uma lista de funções de filtro 
# e uma lista de dados, e retorna uma lista apenas com os elementos que satisfazem todas as condições das funções de filtro.

def filtro_composto(filtros, lista):
    result = lista
    for func in filtros:
        result = list(filter(func, result))
    return result

filtros = [lambda x: isinstance(x, int), lambda x: x % 2 == 0, lambda x: x > 0]
lista = [1, 0, 2, 3, -5, 7, 8, -10, 'a', 'b', 6, 22, 22.1]

print(filtro_composto(filtros, lista))
