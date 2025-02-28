# Exercício 6: Crie uma função que receba uma string e retorne True se ela for
# um palíndromo (uma palavra ou frase que se lê da mesma forma de trás para
# frente) e False caso contrário.

palavra = input("Informe uma palavra: ")

def palindromo (palavra):
    return palavra == palavra[::-1]        
               
print(palindromo(palavra))