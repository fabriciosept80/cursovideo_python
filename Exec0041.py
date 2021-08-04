#A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre
#sua categoria , de acordo com a idade:

# até 9 anos = mirim
# até 14 anos = infantil
# até 19 anos = junior
# até 20 anos = senior
# acima = master
from datetime import date
print("")
print("=+"*30,"\033[1;33mCONFEDERAÇÃO NACIONAL DE NATAÇÃO\033[m","+="*32)
print("categorias de natação".upper().center(153))
hoje = date.today().year
birth = int(input("Digite o ano de nascimento: "))
idade = hoje - birth
if idade <= 9:
    print("O atleta nascido em {} tem {} anos e esta na categoria mirim!".format(birth,idade))
elif idade <= 14:
    print("O atleta nascido em {} tem {} anos e esta na categoria infantil!".format(birth, idade))
elif idade <= 19:
    print("O atleta nascido em {} tem {} anos e esta na categoria júnior!".format(birth, idade))
elif idade <= 25:
    print("O atleta nascido em {} tem {} anos e esta na categoria senior!".format(birth, idade))
else:
    print("O atleta nascido em {} tem {} anos e esta na categoria master!".format(birth, idade))