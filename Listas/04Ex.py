# 4.Verificar se um número específico está presente na lista.

n = [1,2,3,4,5,6,7,8,9,10]
num = int(input("Digite um número de 1 a 10: "))

for i in n:
    if num in n:
        n.remove(num)  
print(n)
    
    
