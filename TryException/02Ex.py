# Crie uma função ler_inteiro() que solicita ao usuário um número inteiro.
# Se o usuário inserir um valor inválido (não inteiro), 
# exiba uma mensagem e peça a entrada novamente até que um número válido seja fornecido.

def ler_inteiro():    
    while True:     
            entrada = (input('Informe um número inteiro (ou "sair" para encerrar o programa): '))

            if entrada.lower() == 'sair': # condição para saída do programa
                 print("Programa encerrado.")
                 return None
            
            try:
                inteiro = int(entrada) # transformar o valor da entrada em inteiro            
                print(f"Você informou {inteiro} que é um número inteiro. Obrigada.")
                return inteiro      
       
            except ValueError: # não sendo possível tratar o erro
                print('Você digitou um caracter inválido, digite apenas número.') 
                print("Entrada inválida! Por favor, insira um número inteiro ou digite 'sair' para encerrar.")

ler_inteiro()
        