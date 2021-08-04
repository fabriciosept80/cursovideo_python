#Faça um programa que peça um nome e verifique se existe "SILVA" no nome
nome = str(input("Entre com seu nome completo: ")).strip()
nome = nome.upper()
if "SILVA" in nome:
    print(f'O cidadão {nome} tem SILVA no nome')
else:
    print(f'O cidadao {nome} não tem SILVA no nome')