# Exercício 9: Crie uma função que conte quantas vogais existem em uma string
# fornecida.

palavra = "amor"
vogais = "aeiou"
nvogais =0 

def cont_vogais (palavra, vogais, nvogais):
    for v in palavra:
        if v in vogais:            
            nvogais += 1          
    print(f'A palavra {palavra} possui {nvogais}')
cont_vogais(palavra, vogais, nvogais)

