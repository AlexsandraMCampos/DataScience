# 2. Faça um programa que receba dois números inteiros e gere os números
# inteiros que estão no intervalo compreendido por eles.

n = int(input("Digite um número: "))
n1 = int(input("Digite um novo número: "))

if n > n1:  # adicionamos essa condição para que o primeiro numero seja menor
      n, n1 = n1, n

for i in range (n+1, n1, 1): 
      print(i)