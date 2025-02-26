# 25 Criar uma lista com 5 elementos e verificar se um número específico está presente.


numero = [1,21,76,42,49]
n= 21

for i in numero:
    if n in numero:
        print(f"O número procurado está na lista.")
        break
        
else:
    print("O número procurado não está na lsita.")
           