#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio, indo de 10 até 0
# com uma pausa de 1 segundo entre eles.

from time import sleep
b=33
for x in range (10,-1,-1):
    sleep(1)
    print(x,end=' ')
print("")
print("Feliz ano novo")