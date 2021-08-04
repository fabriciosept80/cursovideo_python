#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuario vai continuar
#No final mostre.
# Qual é o total gasto na compra
#Qtos produtos custam mais de 1000
#Qual o nome do produto mais barato
soma = menor = cont = caro = 0
barato = ''
print('\033[1;33m<>\033[m'*50)
print('mercadinho felizberto'.upper().center(110))
print('\033[1;33m<>\033[m'*50)
print('')
while True:
    nome = str(input('Digite o nome do produto:R$ ')).upper().strip()
    valor = float(input('Digite o preço do produtuo: '))
    cont += 1
    soma += valor
    if cont == 1:
        menor = valor
        barato = nome
    if valor < menor:
        menor = valor
        barato = nome
    if valor > 1000:
        caro +=1
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    if continua == 'N':
        break
print('#'*50)
print(f'O total gasto na compra foi de R${soma:.2f}.')
print(f'São {caro} com preço acima de R$ 1000.00')
print(f'O produto mais barato é {barato} que custa R$ {menor:.2f}')
print('#'*50)
