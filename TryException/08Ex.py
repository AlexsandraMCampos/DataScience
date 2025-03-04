# Crie uma função contar_caracteres(texto, caractere) que conta quantas vezes um caractere aparece em um texto.
# Se texto não for uma string, exiba um erro.

texto = input("Digite um texto: ").upper()
caractere = input("Digite o caractere que deseja contar: ").upper()

def contar_caracteres(texto, caractere):
    if not isinstance(texto, str):
        return "Erro: O primeiro argumento deve ser uma string."
    if not isinstance(caractere, str) or len(caractere) != 1:
        return "Erro: O segundo argumento deve ser um único caractere."

    contagem = texto.count(caractere)  # Conta quantas vezes o caractere aparece no texto
    return contagem

resultado = contar_caracteres(texto, caractere)
print(f"O caractere '{caractere}' aparece {resultado} vezes no texto.")


       