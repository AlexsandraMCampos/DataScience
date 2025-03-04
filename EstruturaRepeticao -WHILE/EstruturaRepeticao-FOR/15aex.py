# 15. Uma loja tem tem uma política de descontos de acordo com o valor da
# compra do cliente. Os descontos começam acima dos R$500. A cada 100
# reais acima dos R$500,00 o cliente ganha 1% de desconto cumulativo até
# 25%.

for valor in range(500,3100,100):
    desconto = min((valor - 500) // 100 + 1, 25)
    valor_final = valor - (valor *(desconto/100))
    print(f"O valor da compra é de {valor}, o valor do descotnto é de {desconto} e o valor final da compra é {valor_final}")