#3. Somar números até o usuário digitar 0. Peça números ao usuário e
#some-os até que ele digite 0.


num = int(input("Digite um número: ")) # input utilizado para iniciar o programa. Ela sõ é utilizada uma única vez.
soma = 0

while num != 0 :
    soma += num
    num = int(input(" Digite um número (ou 0 para sair): ")) # variavél dentro para eu poder sair do looping
    print(f"A soma é {soma}.")    