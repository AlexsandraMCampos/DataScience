# 12. Numa eleição existem três candidatos. Faça um programa que peça o
# número total de eleitores. Peça para cada eleitor votar e ao final mostrar o
# número de votos de cada candidato.

eleitores = int(input("Informe o número total de eleitores: "))
candA = 0
candB = 0
candC = 0
invalido = 0

for i in range(eleitores):
    voto = input("Escolha entre os 3 votos (A),(B),(C): ").upper()
    if voto == "A":
        candA+=1
    elif voto == "B":
        candB+=1
    elif voto == "C":
        candC+=1        
    else:
        invalido+= 0
        print("Voto inválido.")

print(f"Os candidatos A,B e C receberam respectivamente {candA},{candB},{candC} votos.")

if candA >=candB and candA>candC:
    print(f"O candidato A venceu com {candA} votos.")
elif candB >=candA and candB>candC:
    print(f"O candidato B venceu com {candB} votos.")
elif candC >=candA and candC>candB:
    print(f"O candidato C venceu com {candC} votos.")
else:
    print(f"O total de votos inválidos foi de {invalido}.")
    
    
