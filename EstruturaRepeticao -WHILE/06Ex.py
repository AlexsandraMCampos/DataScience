# 6. Some todos os números pares de 1 a 100 e mostre o resultado.

n = 0
soma = 0

while n <= 100: # quanto o número for menor que 100
        print(n)
        n += 2 # soma mais um
        soma += n
print(f"A soma é {soma}")