#Crie um programa que leia um numero Real qualquer pelo teclado e mostre na tela sua porção inteira. Ex: 6.127
#terá que exibir apenas 6
from math import trunc
n = float(input("Entre com um numero qualquer: "))
print(f"A parte inteira de {n} é {trunc(n)}")
print("O número {} tem a sua parte inteira de {}".format(n,int(n)))