# 7. Considere dois países: A com 80.000 habitantes e 
# taxa de crescimento anual de 3%, e B  com 200.000 habitantes 
# e taxa de 1,5%. Determine quantos anos serão necessários para  
# que a população do país A 
# ultrapasse a população do país B. 

A = 80000
B = 200000
anos = 0

while True:
    A += 0.03 *A
    B += 0.015 *B
    anos += 1
    if A > B:
        break
print(f" A população de A é {A:.0f} habiltantes e levou {anos} anos para ulrapassar a população B." )
        
