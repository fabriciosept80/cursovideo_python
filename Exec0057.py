#Faça um programa que leia o sexo de uma pessoa , só aceite os valores M ou F. Caso esteja errado , peça a digitação
#novamente até ter um valor correto.

s= str(input('Digite o sexo da pessoa [M/F]: ')).upper().strip()[0]
while s not in 'MF':
    s=str(input('Valores incorretos, digite novamente [M/F]: '))
print(f'O valor digitado foi {s}')

