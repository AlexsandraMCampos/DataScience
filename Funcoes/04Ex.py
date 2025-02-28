# Exercício 4: Crie uma função que calcule o fatorial de um número.

n = int(input("Digite um número: "))

def fatorial(n):
    resultado = 1
    for i in range(1,n+1): 
        resultado *=i # a função está pegando o número anterior e multiplicando pelo seguinte
    return resultado

# print(fatorial(n))    

print(f"O valor fatorial do número {n} é {fatorial(n)}")