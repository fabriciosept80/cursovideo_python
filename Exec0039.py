#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
#Se ele ainda vai se alistar no serviço militar
#Se é a hora de se alistar
#Se já passou do tempo de alistamento

#Deverá apresentar também o tempo que falta ou que passou do prazo.

from datetime import date
print("")
print("\033[1;32m - ALISTAMENTO MILITAR - \033[m")
print("")
birthday = int(input("Qual o ano do seu nascimento: "))
today = date.today().year
idade = today - birthday
if idade < 18:
    print(f"Faltam {abs(18 - idade)} anos para se alistar")
elif idade > 18:
    print(f"Já passou do tempo de alistamento em {abs(idade - 18)} anos.")
elif idade == 18:
    print("Já é tempo de se alistar!!")
print("\033[1;33mTenha um ótimo dia!!!\033[m")
