# 2. Escreva um programa que leia um número inteiro positivo e determine se ele é um
# palíndromo (ou seja, se lido de trás para frente continua igual).
# Exemplo:
#  Entrada: 1221
#  Saída: 1221 é um número palíndromo

n = int(input("Digite um número inteiro e positivo:")) 

original= n 
inverso = 0
while n > 0:
        digito = n %10
        inverso = inverso *10 + digito
        n = n // 10
if original  == inverso:
        print(f"{original} é um palindromo.")
else:
        print(f"O número {original} Não é um palindromo.")
        
        
        
