#Crie um programa que mostre na tela dos os numeros pares que estão no intervalo de 1 e 50.

for x in range(1,52):
    if x % 2 == 0:
        print(x,end='-')