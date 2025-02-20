# 10. Uma loja deseja cadastrar 5 clientes e verificar se o faturamento da loja A
# foi superior a loja B (faturamento = 54000). Se o faturamento atingir esse
# valor mostre na tela uma mensagem contendo em quanto foi superado o
# faturamento.

lojab = 54000
total = 0

for i in range (5):
    nota= float(input("informe o valor da sua fatura: "))
    total += nota
if total > lojab:
    diferenca = total - nota
    print(f"O faturamento da loja A foi superado o faturamento da loja B em {diferenca} ")
else:
    print(f"O faturamento da loja A não superou o faturamento da loja B.")


