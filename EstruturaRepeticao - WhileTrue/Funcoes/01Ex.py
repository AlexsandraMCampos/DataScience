#  Exercício 1: Crie uma função que receba dois números como parâmetros e
# retorne a soma deles.

n = int(input("Digite um número: "))
n1 = int(input("Digite outro número: "))

def soma (n,n1):
    return n+ n1

print(f"A soma dos números {n} e {n1} é {soma(n,n1)}")