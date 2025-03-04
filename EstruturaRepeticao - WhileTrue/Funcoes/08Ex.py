# Exercício 8: Crie uma função que receba uma lista de notas e retorne a média
# das notas.

notas =[7,8,9,6]

def media_lista(notas):
        return sum(notas)/len(notas)

print(f"Sua média é {media_lista(notas)}")