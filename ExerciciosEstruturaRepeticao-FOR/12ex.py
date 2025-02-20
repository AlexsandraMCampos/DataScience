# 12. Numa eleição existem três candidatos. Faça um programa que peça o
# número total de eleitores. Peça para cada eleitor votar e ao final mostrar o
# número de votos de cada candidato.

eleitores = int(input("Informe o número total de eleitores:"))
candA= 0
candB =0
candC=0

for i in range(eleitores):
    candidato = input("Escolha entre os 3 candidatos (A),(B),(C): ").upper()
    if candidato == "A":
        candA+=1
    elif candidato == "B":
        candB+=1
    elif candidato == "C":
        candC+=1
print(f"Os candidatos A,B e C receberam respectivamente {candA},{candB},{candC} votos.")

if candA >=candB and candA>candC:
    print(f" O candidato A venceu com {candA} votos.")
elif candB >=candA and candB>candC:
    print(f" O candidato A venceu com {candB} votos.")
else:
    print(f" O candidato A venceu com {candC} votos.")    
    
