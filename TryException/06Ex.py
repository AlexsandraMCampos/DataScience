# Crie uma função multiplicar(a, b) que retorna o produto de a e b.
# Se os valores não forem números, capture a exceção e exiba uma mensagem de erro.


a = input("Informe o primeiro número: ")
b = input("Informe o segundo número: ")

def multiplicar(a,b):    
    try:
        a = int(a)
        b = int(b)

        mult = a * b
        print(f"Os números são {a} e {b}.")
        print(f"E a multiplicação deles é {mult}.")
        return mult
        
    except ValueError:
            print("Os valores informados precisam ser númericos.")  # Mensagem de erro para valores não numéricos
multiplicar(a,b)