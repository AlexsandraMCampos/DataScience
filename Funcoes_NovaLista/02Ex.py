# 2. Crie uma função que recebe uma lista de números e retorna a quantidade de números positivos.

lista = [1,-21,-76,49]

def positivo(lista):
    contpositivo =0
    for i in lista:
        if i > 0:
            contpositivo +=1
        # return contpositivo
    print(f"Os números positivos são {contpositivo}. ")
positivo(lista)
