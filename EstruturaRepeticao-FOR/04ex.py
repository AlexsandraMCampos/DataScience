# 4. Faça um programa que leia 5 números e informe a soma e a média dos
# números.

soma =0

for i in range(1,6):
    n = int(input(f"Digite o {i} número: ")) # input dentro do for por que receberemos 5 números
    soma += n
media =soma/i # meida fora do for por que está não precisa ser repetida
print(f"A soma é {soma} e a média é {media}")

    
