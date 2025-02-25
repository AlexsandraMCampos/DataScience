# 6. Solicite ao usuário uma nota entre 0 e 10. 
# Caso o valor seja inválido, peça novamente até  que o 
# usuário informe um valor válido. 

nota = 0

while True:
    n= int(input("Informe sua nota: "))
    nota += 1
    if n >=0  and n<=10:
       print(n)
    else:
        print("Nota inválida.")

    
  



    

