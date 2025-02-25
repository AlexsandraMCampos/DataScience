# 3.Escreva um programa que leia um número inteiro e conte quantos dígitos ele tem.
# Exemplo:
# Entrada: 98765
# Saída: O número 98765 tem 5 dígitos


n = int(input("Informe um número: "))

for i in range (1):
    conversao = len(str(abs(n)))
    print(f"O número digitado foi {n} e este tem {conversao} digitos.")
