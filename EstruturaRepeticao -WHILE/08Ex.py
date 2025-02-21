# 8. Encontrando o maior número inserido pelo usuário. Peça números ao
#usuário e, ao digitar 0, exiba o maior número inserido.

n = int(input("Digite um número: "))
n1 = 0

while n != 0:
    if n > n1: #
        n1 = n
    n = int(input("Digite um número: "))        
print(f"O maior número é {n1}.")





