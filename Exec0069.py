#Crie um programa que leia a idade e o sexo de varias pessoas. A cada pessoa cadastrada, o programa deverá perguntar
#se o usuário quer continuar ou não. No final mostre :
#a)qts pessoas tem mais de 18 anos
#b)qtos homens foram cadastrados
#c)Qtas mulheres tem menos de 20 anos.

maisdezoito = homens = mulheres = 0
print('#'*45)
print('CADASTRO DE PESSOAS'.center(40))
print('#'*45)
while True:
    idade = int(input('Entre com a idade da pessoa: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Entre com o sexo da pessoa [M/F]: ')).strip().upper()[0]
    continuar= ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar ? [S/N]:')).upper().strip()
    if continuar != 'S':
        break
    if idade >= 18:
        maisdezoito +=1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres +=1
print('*'*50)
print(f'Total de pessoa com mais de 18 é {maisdezoito} pessoa.' if maisdezoito <= 1 else f'Total de pessoas com mais de 18 é {maisdezoito} pessoas')
print(f'Total de homem é {homens} pessoa.' if homens <= 1 else f'Total de homens são {homens} pessoas.')
print(f'Total de mulher com menos de 20 anos é de {mulheres} pessoa' if mulheres <= 1 else f'Total de mulheres com menos de 20 anos é de {mulheres} pessoas')
print('*'*50)
