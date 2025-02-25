# 10. Implemente um sistema de votação onde o usuário pode votar em candidatos (1 a 4), nulo
# (5) ou branco (6). O programa deve exibir o total de votos de cada tipo e a porcentagem de
# votos nulos e brancos. A entrada 0 encerra a votação.

# escolher um candidato
# contar o total por candidato
#  contar o total dos eleitores
# somar total dos votos por eleitor
# porcentagem por candidato

votos = [0, 0, 0 ,0 , 0 , 0]

while True:
    voto = int(input("Informe o número do seu candidato: "))
    if voto  == 0: # condiçao de saída
        print("Voto inválido.")
        break
    if 1 <= voto <=6:
        votos[voto-1] += 1
    else:
        print("Voto inválido. Insira um voto válido.")


total_votos = sum(votos)
porcetagem_nulo = (votos[4]/total_votos)*100
porcentagem_branco = (votos[5]/total_votos)*100
for i in range(4):
    print(f"Candidato {i+1}: {votos[i]} votos")
print(f" Votos nulo: {votos[4]}")
print(f" Votos brancos: {votos[5]}")
print(f"Porcentagem de nulos {porcetagem_nulo:.2f} %")
print(f"Porcentagem de brancos {porcentagem_branco:.2f} %")
       
   


