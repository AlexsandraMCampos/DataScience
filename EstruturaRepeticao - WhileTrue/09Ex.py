# 9. Implemente um sistema onde o usuário insere o código e a quantidade dos produtos  desejados.
# O programa deve calcular o valor total e permitir que o usuário finalize o  pedido digitando 0. 

#  Criei um dicionário para armazenar itens e preços
precos = {
    1: 9.00,  # café expresso
    2: 8.00,  # capuccino
    3: 4.50,  # chá
    4: 2.50   # leite
}

# Iniciando Variáveis
total =0
pedido =[]

while True:
     codigo = int(input("Escolha seu pedido (1- café expresso, 2- cappuccino, 3-chá, 4- leite) ou 0 para sair: "))

     if codigo == 0:
          print("Volte sempre.")       
          break
     if codigo not in [1,2,3,4]:
          print("Código inválido. Por favor digite um código válido.")
          continue
     quantidade = int(input("Informe a quantidade desejada: "))
     pedido.append({"código": codigo, "quantidade": quantidade})

     subtotal = precos[codigo]*quantidade

     total += subtotal
     print(f"O total do seu pedido foi R$ {total}")

     resumo_pedido = ["", "Café Expresso", "Capuccino", "Chá", "leite"][codigo]
     print(f"Pedido: {quantidade}x{resumo_pedido} - {subtotal:.2f}")



     








