# 7. Crie uma função que recebe uma lista de números e retorna a soma
# apenas dos números pares.

n =[1,2,3,4,5,6,7,8,9,10]

def soma_pares(n):
        pares = [num for num in n if num%2 == 0] # num para os itens em n
        return sum(pares)

print(f"Somas dos número pares: {soma_pares(n)}")