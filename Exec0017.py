#Faça um programa que leia o comprimento do cateto oposto de do cateto adjacente de um triangulo retangulo, calcule e
#mostre o comprimento da hipotenusa.

import math

oposto = float(input('Entre com o valor do cateto oposto: '))
adja = float(input("Entre com o valor do cateto adjacente: "))
hip = math.hypot(adja,oposto)
print("O valor da hipotenusa é de {:.2f}:".format(hip))