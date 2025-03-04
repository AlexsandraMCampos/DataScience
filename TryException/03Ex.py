#Crie uma função calcular_media(numeros) que recebe uma lista de números e retorna a média.
# Se a lista estiver vazia, a função deve tratar a exceção e exibir uma mensagem adequada.

lst = [1,2,3,4,5,6,7,8,9,10]

def calcular_media(numeros):
    try:
        if not numeros:
            raise ValueError("A lista está vázia. Não é possível calcular média.")
        
        s = sum(numeros)
        m = s + len(numeros)
        return m    
    except ValueError as e:
            print(e)
            return None
   

# Testando com uma lista válida
print(f"Média: {calcular_media(lst)}")  # Deve imprimir a média correta

# Testando com lista vazia
print(f"Média: {calcular_media([])}")  # Deve exibir mensagem de erro e retornar None
