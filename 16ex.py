# 16. Faça um programa que receba a idade de 15 pessoas 
# e que calcule e 
# mostre:
# a) A quantidade de pessoas em cada faixa etária;
# b) A percentagem de pessoas na primeira e na última faixa etária, com
# relação ao total de pessoas:
#  Até 15 anos
#  De 16 a 30 anos
#  De 31 a 45 anos
#  De 46 a 60 anos
#  Acima de 61 anos

crianca = 0
adolescente = 0
adulto = 0
meiaidade = 0
senior = 0


for i in range(15):
    idade = int(input("Informe sua idade: "))
    if idade > 0 and idade < 15:
        crianca +=1
    elif idade > 16 and idade < 30:
        adolescente +=1      
    elif idade > 31 and idade < 45:
        adulto +=1        
    elif idade > 46 and idade < 60:
        meiaidade +=1        
    else:
        print()

print(f"O número de crianças é {crianca}.")
print(f" A porcentagem de crianças é {(crianca/15)*100}")
print(f"O número de adolescente {adolescente}.") 
print(f"O número de adulto {adulto}.")
print(f"O número de pessoas de meia idade é {meiaidade:.2f}.")
print(f" A porcentagem de pessoas de meia idade  é {(meiaidade/15)*100}")