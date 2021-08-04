#Crie um programa que leia o nome completo de uma pessoa e mostre :
# O nome com todas as letras maiusculas
# O nome com todas as letras minusculas
# Quantas letras ao todo sem cosiderar espaços.
# Quantas letras tem o primeiro nome

nome = str(input("Digite seu nome completo: ")).strip()
print("O nome em maiuscula é :",nome.upper())
print("O nome em minúscula é : ",nome.lower())
print("A quantidade de caracteres descontado o espaço são :",len(nome)-nome.count(' ')) # para tirar espaços ele faz a leitura do nome e subtrai os espaços com o nome.count ('')
print(f"A quantidade de letras do primeiro nome que é {nome.split()[0]} são : ",len(nome.split()[0]))

