#Melhore o jogo do desafio 028 onde o computador vai "pensar" em um numero entre 0 e 10. Só q agora o jogador vai tentar
#adivinhar até acertar , mostrando no final quantos palpites foram necessários para vencer.

import random

n = [0,1,3,4,5,6,7,8,9,10]
cont = 1
respComp = random.choice(n)
respUser = int(input("Digite um numero entre [0 e 10]: "))
while respComp != respUser:

    if respUser < respComp:
        respUser = int(input("Número errado. Tente novamente: "))
        cont += 1
        print('Tente um numero maior')
    else:
        respUser = int(input("Número errado. Tente novamente: "))
        cont += 1
        print('Tente um numero menor')
print(f'Parabéns, você acertou em {cont} palpites !')

