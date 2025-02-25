# 5. Escreva um programa que leia um número inteiro positivo e determine se ele é um
# quadrado perfeito (ou seja, se existe um número inteiro x tal que x² = n).
# Exemplo:
#  Entrada: 49
#  Cálculo: 7 × 7 = 49
#  Saída: 49 é um quadrado perfeito

n = int(input("Digite um número: "))
x = 0

while x * x <= n:
    if x*x == n:
        print(f"O número {n} é um quadrado perfeito.")
        break
    x +=1
else:
    print(f"O número {n} não é um quadrado perfeito.")
