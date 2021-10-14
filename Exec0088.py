#Faça um programa que ajude um jogador da MegaSena a criar palpites. O programa irá perguntar quantos jogos serão
#gerados e vai sortear 6 numeros entre 1 e 60, para cada jogo, cadastrando tudo em uma lista composta.
import random
from random import sample
from time import sleep
count1 = 0
jogo = list()
numero = list()
print("#"*10,'Good Luck - Loterias',"#"*10)
print()
njogos = int(input('Quantos jogos voce quer fazer : '))

while count1 <= njogos-1:
    count = 0
    while True:
        n = (random.randint(1,60))
        if n not in numero:
            numero.append(n)
            count += 1
        if count >= 6:
            break
    numero.sort()
    jogo.append(numero[:])
    numero.clear()
    count1 += 1
print(f'$*'*10,'Gerando ',njogos,'jogos !!!','*$'*10)
for i, j in enumerate(jogo):
    print(f'Jogo {i+1} : {j}')
    sleep(1)
print("$*"*10,'--Boa Sorte--',"*$"*10)