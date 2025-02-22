# 4. Solicite ao usuário que insira números. O programa deve continuar até que um número
# negativo seja inserido. No final, exiba o maior número informado.
n = 1
numeros = []

while n > 0:
    n = int(input("Digite um número: "))
    if n < 0:
        break
    numeros.append(n)
print(f"O maior número digitado foi {max(numeros)}") 
              






