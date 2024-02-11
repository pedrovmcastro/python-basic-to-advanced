# 1). Crie uma função de alta ordem chamada aplica_funcao que recebe uma função funcao e uma lista dados e retorna uma lista com a aplicação 
# da função em cada elemento da lista.

def aplica_funcao(funcao, dados):
    return list(map(funcao, dados))

def funcao(num):
    return num * num

print(aplica_funcao(funcao, [1, 2, 3, 4, 5]))
