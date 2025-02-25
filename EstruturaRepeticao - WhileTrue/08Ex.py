# 8. Implemente um sistema de caixa registradora onde o usuário insere valores dos produtos.  
# A entrada de 0 indica o fim da compra. Exiba o total da compra, peça o valor pago e exiba  o troco. 
# Após isso, o programa deve reiniciar para um novo cliente. 

while True:
    preco_total = 0

    while True:
        preco = float(input("Informe o preço do produto ou 0 para finalizar. R$: "))
        if preco == 0:
            break

        preco_total += preco
        print(f"Total da compra: R$ {preco_total:.2f}")

    while True:
        valor_pago = float(input("Informe o valor pago R$ "))
        if valor_pago >= preco_total:
            break
        print(f"Valor insuficiente!Valor total da compra R${preco_total}")
    
    troco = valor_pago - preco_total
    print(f"Troco: R$ {troco:.2f}")
    continuar = input("\nDeseja atender outro cliente? (s/n): ")
    if continuar.lower() != 's':
        break

print("\nCaixa fechado!")
    

    





