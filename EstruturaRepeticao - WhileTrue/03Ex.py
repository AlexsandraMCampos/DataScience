# 3. Peça ao usuário que insira notas (valores numéricos). A entrada deve continuar até que o
# usuário digite -1. Em seguida, exiba a média das notas.

nota = 0
soma = 0
contador = 0

while nota != -1:
    nota = int(input("Digite sua nota ou -1 para sair: "))
    if nota !=-1:
        soma += nota
        contador += 1
media = soma/contador   
print(f"Sua média é {media}.")    
