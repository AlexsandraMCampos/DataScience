# 3. Faça um programa que verifique e mostre os números entre 1.000 e 2.000
# que, quando divididos por 11 produzam resto igual a 2.

n = 1000
n1 = 2001
numero = 0
for i in range(1000, 2001, 1):
    if i%11 == 2:
        print(i)
    
