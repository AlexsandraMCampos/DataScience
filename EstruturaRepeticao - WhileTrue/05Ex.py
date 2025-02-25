# 5. Solicite ao usuário números indefinidamente. O programa deve parar quando o usuário  
# digitar um número igual ao anterior. Em seguida, exiba quantos números foram inseridos. 

lista = [] # lista vazia para adicionar o números digitados

while True:
    n = int(input("Digite um número: ")) # solicitação do número para o usuário
    # numero += 1   
    if lista and n == lista[-1]: #condição se o último número da lista for igual ao último número digitado
        break
    lista.append(n) # adiciona os números digitados a lista
print(f"Foram digitados {len(lista)} números.")    
print(f"Os números digitados foram {lista}.")    
