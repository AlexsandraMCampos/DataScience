# 9. Contar quantos números pares o usuário digitar. O programa deve
# contar quantos números pares o usuário inseriu. O usuário para
# digitando -1.

n = int(input("Digite um número: "))
par = 0

while n != -1: 
    if n %2 == 0: 
        par += 1
    n = int(input("Digite um novo número (ou -1 para sair): "))        
print(f"Você digitou {par} números pares.")
       
       
       
       
