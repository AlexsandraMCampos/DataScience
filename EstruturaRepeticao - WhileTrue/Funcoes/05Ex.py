# Exercício 5: Crie uma função chamada tabuada que recebe um número e
# imprime sua tabuada do 1 ao 10.

n = int(input("Digite um número: "))


def tabuada (n):
    for i in range(1,11):
       print(f"{n} x {i} = {n*i}")
tabuada(n)

