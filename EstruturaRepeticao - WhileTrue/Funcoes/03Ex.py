# Exercício 3: Crie uma função chamada media_lista que recebe uma lista de
# números e retorna a média deles.

lista = [1,21,76,49]

def media_lista(lista):
        return sum(lista)/len(lista)

print(f"A média da lsita é {media_lista(lista)}")
