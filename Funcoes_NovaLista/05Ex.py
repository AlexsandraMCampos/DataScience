# Crie uma função que recebe uma lista de números e substitui os números negativos por zero.

n = [-3,-2,-1,0,1,2,3]

def trocar_negativo(n):
    lista_positiva = [0 if i < 0 else i for i in n]  # Compreensão de lista para substituir negativos por zero
    return lista_positiva

# Teste da função
n = [-3, -2, -1, 0, 1, 2, 3]
resultado = trocar_negativo(n)
print(resultado)  # Saída esperada: [0, 0, 0, 0, 1, 2, 3]

