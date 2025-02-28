# Crie uma função que recebe duas palavras e retorna True se forem anagramas uma da outra.

p1 = input("Informe uma palavra: ")
p2 = input("Informe uma nova palavra: ")

def anagrama(p1,p2):
    return sorted(p1) == sorted(p2)

print(anagrama(p1,p2))

