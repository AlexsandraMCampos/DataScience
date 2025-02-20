# 9. Faça um programa que peça um número inteiro e determine se ele é ou
# não um número primo. Um número primo é aquele que é divisível somente
# por ele mesmo e por 1.

num = int(input("Digite um número: "))

if num < 2:
    num= print(f"O número {num} Não é primo.")
else:
    for i in range(2, num):
        if num % i == 0:
            print(f"O número {num} Não é primo.")
            break
    else:
        print(f"O número {num} é primo.")