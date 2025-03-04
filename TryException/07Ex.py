# Crie uma função pegar_elemento(lista, indice) que retorna o elemento de uma lista na posição indice.
# Se o índice não existir, trate o erro.

lst = ["confiança", "fé", "determinação","trabalho","amor","dedicação"]

def pegar_elemento(lst,indice):
    try:
        return lst[indice]
    except IndexError: 
        return "Erro: o índice fora dos limites da lista."  
    except TypeError:
        return "Erro: o índice dever ser um número inteiro." 
    

print(pegar_elemento(lst,3))
                     

    