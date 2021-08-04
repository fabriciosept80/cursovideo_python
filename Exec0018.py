#Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo.

from math import sin,cos,tan,radians
#import math
print(" Calculo do Seno - Cosseno e Tangente => Dado o valor do angulo")
print("")
angulo = float(input("Digite o valor do angulo: "))
#valor = radians(angulo)
#coss = cos(valor)
#print(coss)
print(f"Para o angulo de {angulo} temos como Seno {sin(radians(angulo)):.3f} \n e temos como Cosseno {cos(radians(angulo)):.3f} \n e como Tangente temos {tan(radians(angulo)):.3f}")