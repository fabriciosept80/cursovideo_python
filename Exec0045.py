#Pedra ganha da tesoura (amassando-a ou quebrando-a).
#Tesoura ganha do papel (cortando-o).
#Papel ganha da pedra (embrulhando-a).
import random
import sys
from time import sleep

print("")
a = "\033[7;34mJO\033[m";b = "\033[7;33mKEN\033[m".center(-180);c = "\033[7;38mPÔ\033[m"
print(a.center(80),end='')
sleep(1)
print(b.center(0),end='')
sleep(1)
print(c.center(80))
#sleep(1),print("\n"*100,end=''),print(a,b,c)
print("")
count = 0
drawn = 0;win = 0; lost = 0
def playagain(play):
    play = str(input("Deseja jogar novamente: Digite \033[1;35mSIM\033[m ou \033[1;39mNÃO\033[m: ")).strip().upper()
    if play != "SIM":
        print("\n"*100)
        print(f"You played {count} games!!!".center(150).title())
        result = (f"Você venceu \033[1;32m{win} => {(float(win/count)*100):.2f}%\033[m das partidas, empatou \033[1;33m{drawn} => {(float(drawn/count)*100):.2f}%\033[m das partidas e perdeu \033[1;31m{lost} => {(float(lost/count)*100):.2f}%\033[m das partidas")
        print('\033[1;40m',result.upper().center(180),'\033[m ')
        print("\033[7;31m#"*70,"\033[m","END GAME","\033[7;31m#"*70,"\033[m")
        sys.exit()
sleep(2)
play = str(input("Gostaria de jogar JUNKENPÔ ! Digite \033[7;32mSIM\033[m ou \033[7;31mNÃO\033[m: ")).strip().upper()
if play == 'SIM':

    while play != "NÃO":
        valorcomput = ['PEDRA','PAPEL','TESOURA']
        valor = str(input("Digite \033[1;32mPEDRA\033[m || \033[1;33mPAPEL\033[m || \033[1;31mTESOURA\033[m : ")).strip().upper()
        aleatorio = random.choice(valorcomput)

        if valor == 'PEDRA' and aleatorio == 'PEDRA' or valor == 'TESOURA' and aleatorio == 'TESOURA' or valor == 'PAPEL'   and aleatorio == 'PAPEL':
            print(f"You DRAWN. You selected a {valor} and the laptop selected {aleatorio}")
            drawn += 1
            count += 1
            playagain(play)
        elif valor == 'PEDRA' and aleatorio == 'TESOURA':
            print(f"You win. You selected a {valor} and the laptop selected {aleatorio}.{valor} ganha da {aleatorio} (amassando-a ou quebrando-a).")
            win += 1
            count += 1
            playagain(play)
        elif valor == 'TESOURA' and aleatorio == 'PAPEL':
            print(f"You win. You selected a {valor} and the laptop selected {aleatorio}.{valor} ganha da {aleatorio} (cortando-a).")
            win += 1
            count += 1
            playagain(play)
        elif valor == 'PAPEL' and aleatorio == 'PEDRA':
            print(f"You win. You selected a {valor} and the laptop selected {aleatorio}.{valor} ganha da {aleatorio} (embrulhando-a).")
            win += 1
            count += 1
            playagain(play)
        else:
            print(f"You lost. You selected {valor} and the laptop selected {aleatorio}")
            lost += 1
            count += 1
            playagain(play)

    else:
        print("END GAME")
        pass

