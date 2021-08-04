#Escreva um programa que leia um numero inteiro qualquer e peça para o usuario escolher qual será a base de conversao:
#1 - para binário
#2 - para octal
#3 - para hexadecimal

cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m',
         'verde': '\033[1;32m',
         'vermelho':'\033[7;31m'}

#print('''Esolha uma das bases para conversão:
#[1] - Converter para Binário
#[2] - Converter para Octal
#[3] - Converter para Hexadecimal''') # Opção para fazer menus.
# usar o fatiamento para tirar as referencias de hex, bin e octal.
print("")
print(cores['amarelo'],"*"*60,"CONVERSAO DE BASES","*"*60,cores['limpa'])
numero = int(input("Digite o número inteiro que deseja converter: "))
x = int(input("Qual a base você deseja transformar : \033[34m 1-BINARIO\033[m \033[33m 2-OCTAL\033[32m 3-HEXADECIMAL\033[m : "))
if x == 1:
    print(f"O número {numero} convertido para BINARIO é:",cores['azul'],bin(numero)[2:],cores['limpa'])#usando o fatiamento para exibir o binario.
elif x == 2:
    print(f"O número {numero} convertido para OCTAL é:",cores['amarelo'],oct(numero)[2:],cores['limpa'])#usando o fatiamento para exibir o binario.
elif x == 3:
    print(f"O número {numero} convertido para HEXADECIMAL é: ",cores['verde'],hex(numero)[2:],cores['limpa'])#usando o fatiamento para exibir o binario.

