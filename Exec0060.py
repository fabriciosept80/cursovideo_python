#Faça um programa que leia um numero quaquer e mostre o seu fatorial
import math
n=int(input("Digite um numero qualquer: "))
numero = n
fator = []
n = n + 1
while n >= 2:
    n = n - 1
    fator.append(n)
valor = math.factorial(numero)
lst_new = [str(a) for a in fator]
print(f'{numero}!=',end='')
print(*lst_new,sep='x',end='')
print(f'={valor}')
