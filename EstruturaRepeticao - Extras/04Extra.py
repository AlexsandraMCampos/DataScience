# 4. Escreva um programa que leia um número inteiro positivo e determine se ele é um número
# perfeito. Um número perfeito é aquele cuja soma dos seus divisores próprios (excluindo ele
# mesmo) é igual ao próprio número.
# Exemplo:
#  Entrada: 28
#  Cálculo: 1 + 2 + 4 + 7 + 14 = 28
#  Saída: 28 é um número perfeito


n = int(input("Digite um número:  "))
soma_divisores = 0 

# Encontrar todos os divisores do números
for i in range(1,n):
    if n % i == 0:
        soma_divisores += i
        print(soma_divisores)
      
     
     # Verificar se o número é perfeito
if soma_divisores == n:
    print(f"O número {n} é um número perfeito e seus divisores são {soma_divisores}.")
else:
    print(f"O número {n} não é um número perfeito.")
        
        

