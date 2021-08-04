#Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o jogador perder,
#mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
vitoria = 0
while True:

    nuser= int(input('Digite um numero [1 a 10]: '))
    tipouser = str(input('Par ou Impar o resultado ?: ')).upper().strip()
    if nuser < 0 or tipouser not in 'PARIMPAR':
        print("="*40)
        print('\033[1;35mFIM DO PROGRAMA\033[m'.center(50))
        print('='*40)
        break

    ncomp = randint(1,10)
    soma = nuser + ncomp
    if tipouser == 'PAR':
        tipocomp = 'IMPAR'
    if tipouser == 'IMPAR':
        tipocomp = 'PAR'
    if soma % 2 == 0 and tipouser == 'PAR':
        print(f'Você venceu, escolheu :{tipouser}'.upper())
        vitoria += 1
    elif soma % 2 == 1 and tipouser == 'IMPAR':
        print(f'Você venceu, escolheu :{tipouser}'.upper())
        vitoria += 1
    else:
        print(f'O computador venceu, escolheu :{tipocomp}'.upper())
        print(f'Você escolheu {nuser} e o computador escolheu {ncomp}, {soma} '.upper())
        print(f'Você venceu {vitoria} vezes')
        print("=" * 40)
        print('\033[1;35mFIM DO PROGRAMA\033[m'.center(50))
        print('=' * 40)
        break
    print(f'Você escolheu {nuser} e o computador escolheu {ncomp}, {soma} '.upper())
