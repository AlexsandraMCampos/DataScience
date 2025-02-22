# 2. Solicite ao usuário que insira uma senha e continue pedindo até que ele insira a senha
# correta definida previamente.

senha = "abrir"
tentativa = input("Digite a senha: ")

while senha != tentativa:
    print("Senha incorreta, tente novamente.")
    tentativa = input("Digite a senha: ")
print("Acesso liberado.")



