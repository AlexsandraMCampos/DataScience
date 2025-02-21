# 7. Adivinhe o número secreto (de 1 a 10). O usuário deve tentar adivinhar
# um número até acertar. (Declare um valor e receba outro)

num_secreto = "7"
tentativa = input("Adivinhe o número secreto de 1 a 10: ")

while num_secreto != tentativa:
    print("Tentativa errada. Tente novamente")
    tentativa = input("Faça uma nova tentativa: ")
print("Você acertou!")