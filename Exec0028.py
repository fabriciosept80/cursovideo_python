#Escreva um programa que faça o computador "pensar" em um numero inteiro entre 0 e 5 e peça para o usuario tentar
#descobrir qual foi o numero escolhido pelo computador. O programa deverá escreve na tela se o usuario venceu ou perdeu.
import random
from time import sleep #biblioteca tempo, comando sleep para aguardar.
#randint (0,5) outra forma de aleatório.
n = [0,1,2,3,4,5]
valor = int(input("Tente acertar o valor gerado pelo computador ente 0 e 5 : "))
comput = (random.choice(n))
print("processando.....")
sleep(2) # para o computador aguardar
if valor == comput:
    print(f'Você acertou o valor. Computador {comput} e você {valor}.')
else:
    print(f'Você errou o valor. Computador {comput} e você {valor}.')