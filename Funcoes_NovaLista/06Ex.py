# Crie uma função que recebe uma lista de palavras e retorna a palavra com mais letras.

nomes = ['Alexsandra', "Michele", "Cibele", "Dulcinéia", "Sofia", "AlexsandraMaria"]

def maior_palavra (nomes):
    nome_maior = nomes[0] # cria uma lista com nomes e considera que o primeiro nome é o maior
    for nome in nomes:
        if len(nome) >= len(nome_maior): # compara cada item da lista com o seguinte e armazena o maior
            nome_maior= nome # o item maior da lista nome é armazenado em nome maior
    return nome_maior

print(maior_palavra(nomes))
    
    