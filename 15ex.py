# 15. Uma loja tem tem uma política de descontos de acordo com o valor da
# compra do cliente. Os descontos começam acima dos R$500. A cada 100
# reais acima dos R$500,00 o cliente ganha 1% de desconto cumulativo até
# 25%.

desconto = 0
descontomax = 25

n = float(input("Informe o valor da compra R$: "))
if n > 500:
    diferenca = n - 500
    intervalo = int(diferenca//100)
    for i in range(intervalo):
      if desconto < descontomax:
            desconto+=1
valordesconto = n *(1-desconto/100)
print(f" O valor da compra  foi R${n:.2f}")
print(f"Desconto aplicado {desconto}%.")
print(f"Valor final R$ {valordesconto:.2f}")
      

     



    
          