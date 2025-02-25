# Escreva um programa que leia um número N e imprima todos os termos da sequência de Fibonacci 
# até que o maior termo seja menor ou igual a N.
# Exemplo:
# Entrada: 20
# Saída: 0 1 1 2 3 5 8 13

# Como resolver:
# - solicitar um número
# - escrever a sequência de Fibonacci deste número
# - apresentar a sequência


n = int(input("Digite um número: "))
a,b = 0,1 

fibonacci = []

while a <= n:
        fibonacci.append(a)
        a,b =b, a+b
print(f"A sequência do {n} é : {fibonacci}")
    