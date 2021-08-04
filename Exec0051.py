#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos
#dessa progressão
import math
p=int(input("Digite o 1º termo da PA : "))
r=int(input("Digite a razão da PA : "))
decimo = p + (11-1) * r # formula da PA, para calcular o decimo termo, ou o termo que vc quiser, coloquei o 11 por causa do python.
for x in range(p,decimo,r):
    print(f'{x}',end='-')
print("FIM")
