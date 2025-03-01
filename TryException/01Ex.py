# 1. Crie uma função chamada calculadora que receba três parâmetros: dois
# números e uma operação (+, -, *, /).
# A função deve retornar o resultado da operação, mas precisa tratar as
# seguintes exceções:
#  Divisão por zero (ZeroDivisionError)
#  Tipo de dado inválido (ValueError)


def calculadora():
        try:
            n=int(input("Digite um número (ou x para sair do sistema): "))
            n1=int(input("Digite um número (ou x para sair do sistema): "))
            operador =input("Informe um operador matemático (+,-,*,/) ou x para sair: ") 
            if operador == "x":
                 print("Até breve.")
            elif operador == "+":
                resultado = n+n1
            elif operador == "-":
                resultado = n - n1
            elif operador =="*":
                resultado = n * n1
            elif operador == "/":
                resultado = n/n1
                if n1 == 0:
                     raise ZeroDivisionError("Não é possível dividir por zero.")
                resultado = n/n1
                    
            else:          
                print("Você não escolheu um operador ou escolheu um comando inválido.")
                return 
            print(f"Operação: {n}{operador}{n1} = {resultado}") 
        except ValueError:
            print("Você digitou um caracter inválido, digite somente números.")
        except ZeroDivisionError as zero:
             print(zero)

calculadora()