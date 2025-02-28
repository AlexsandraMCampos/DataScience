# Exercício 2: Crie uma função que receba um número e retorne &quot;Par&quot; se o
# número for par ou &quot;Ímpar&quot; se o número for ímpar.

n = int(input("Digite um número: "))

def impar_par(n):
    if n % 2 == 0:
        return "Par"
    else:
        return "Impar"
print(f"O número {n} é {impar_par(n)}.")