# 14. Faça um programa que peça uma nota, entre zero e dez. Mostre uma
# mensagem caso o valor seja inválido e continue pedindo até que o usuário
# informe um valor válido.

for i in range(1000):
    nota = float(input("Informe sua nota: "))
   
    if nota > 0 and nota <=10:
        print("Nota válida.")
        break    
    else:  
        print("Nota inválida.")
    
