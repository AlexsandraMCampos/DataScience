# 11. Faça um programa que peça para n pessoas a sua idade, ao final o
# programa deverá verificar se a média de idade da turma varia entre 0 e
# 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou
# idosa, conforme a média calculada.


soma =0

for i in range(1,6):
    n = int(input("Informe sua idade:"))
    soma +=n
    media =soma/i
if media > 0 and media < 26:
    print(f"A média da idade de Voces é {media} e voces são jovens.")
elif media > 26 and media < 60:
    print(f"A média da idade de Voces é {media} e voces são adultos.")
else:
    print(f"A média da idade de Voces é {media} e voces são idosos.")




