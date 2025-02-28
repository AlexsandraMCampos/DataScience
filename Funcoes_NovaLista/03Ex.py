# Crie uma função que recebe uma lista de números e retorna a quantidade de números que são múltiplos de 3.

lista = [1,21,18,49]

def multiplos (lista):
    contmultiplos =0
    for i in lista:
        if i % 3 == 0:
            contmultiplos +=1
        # return contmultiplos
    print(f"Na lista temos {contmultiplos} números que são multiplos de 3.")
multiplos(lista)
