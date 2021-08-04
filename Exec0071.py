#Crie um programa que simule o funcionamento de um caixa eletronico. No inicio, pergunte ao usuario qual será o valor a
#ser sacado (numero inteiro) e o programa vai informar quantas cedulas de cada valor serão entregues. Obs : Considere
#que o caixa possui cédulas de R$ 50 - R$ 20 - R$ 10 - R$ 1.
print('')
print('\033[1;35m{:=^140}\033[m'.format('BANCO 171'))
print('\033[1;34;40m{:=^140}\033[m'.format('SEU PREJUIZO É NOSSA ALEGRIA !!!'))
nota = 50
valor = int(input('Qual o valor a ser sacado: '))
novovalor = valor
novo50 = novo20 = novo10 =0
while novovalor > 10:
    novo50 = valor // nota
    novovalor = valor - (novo50*50)
    nota = nota - 30
    novo20 = novovalor // nota
    novovalor = novovalor - (novo20*20)
    nota = nota - 10
    novo10 = novovalor // nota
    novovalor = novovalor -(novo10*10)
if novo50 != 0:
    print(f'Você recebeu {novo50} notas de R$ 50')
if novo20 != 0:
    print(f'Você recebeu {novo20} notas de R$ 20')
if novo10 != 0:
    print(f'Você recebeu {novo10} notas de R$ 10')
if novovalor != 0:
    print(f'Você recebeu {novovalor} notas de R$ 1')
print('{:=^100}'.format('\033[1;34mOPERAÇÃO FINALIZADA\033[m'))

