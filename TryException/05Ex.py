# Crie uma função soma_lista(numeros) que recebe uma lista de números e retorna a soma.
# Se a lista contiver valores inválidos, capture a exceção e exiba uma mensagem de erro.


lst = [2, 4, 6, 8, 10, 12, "a", "bobeira", "café"]
def soma_lista(lst):
    numeros = []  # Lista para armazenar apenas os números

    for i in lst:
        try:
            numero = int(i)  # Tenta converter para número
            numeros.append(numero)  # Adiciona se a conversão for bem-sucedida
        except ValueError:
            print(f"Valor inválido ignorado: {i}.")  # Mensagem de erro para valores não numéricos

    soma = sum(numeros)  # Calcula a soma dos números filtrados
    
    print(f"A lista limpa apenas com números é {numeros}.")
    print(f"A soma dos números da lista é {soma}.")
    
    return soma  # Retorna o valor da soma

soma_lista(lst)
