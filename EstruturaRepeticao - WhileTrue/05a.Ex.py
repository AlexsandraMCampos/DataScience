anterior = int(input("Digite um número: "))
contador = 0

while True:
    num = int(input("Digite um número: "))
    if num  == anterior:
        break
    contador += 1
    anterior = num
print(f"Quantidade de número inseridos {contador} e o último número foi {anterior}.")
