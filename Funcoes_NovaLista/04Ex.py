# Crie uma função que recebe uma lista de palavras e junta tudo em uma única frase.

palavras = ["Eu", "só", "sei","que","nada", "sei"]

def juntar_palavra(palavras): #recebe uma lista
   return " ".join(palavras) # une as strings da lista
       
frase = juntar_palavra(palavras)
print(f" A frase formada com as palavras é '{frase}'.")
