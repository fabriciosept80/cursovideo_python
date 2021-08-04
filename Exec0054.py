#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram
# a maioridade e quantas já são maiores.
from datetime import date
countM = 0
countm = 0
for x in range (1,8):
    nasc = int(input(f"Digite o ano do nascimento da {x}ª pessoa: "))
    if (date.today().year - nasc) >= 18:
        countM += 1
    else:
        countm += 1
print(f'\033[7;33m{countM}\033[m pessoas são maiores de idade e \033[7;36m{countm}\033[m pessoas são menores de idade')