#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e ultimo nome dela, separada
#mente

nome = str(input("Digite o nome do cidadão: ")).strip()
nome = nome.upper()
print(f"O primeiro nome do cidadão {nome} é : {nome.split()[0]}.")
print(f"O último nome do cidadão {nome} é : {nome.split()[-1]}.")