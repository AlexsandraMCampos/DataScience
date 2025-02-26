# 7.Criar uma lista de strings e verificar quantas vezes uma palavra específica aparece.

palavras =["paz","amor","fé","coragem","amizade","respeito","amizade","confiança","respeito"]

sentimento = input("Informe um sentimento importante para você: ")

for i in palavras:
    if sentimento in palavras:
        print(sentimento)
        break
else:
    print("A palavra digitada não contem na lista.")    