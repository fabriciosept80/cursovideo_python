#Crie um programa que leia 2 valores e mostre um menu na tela :
#[1] somar
#[2] multiplicar
#[3] maior
#[4] novos numeros
#[5] sair do programa
opt = 0
n = int(input('Digite um numero:'))
n1= int(input('Digite outro numero: '))
while opt != 5:
    print('[1] Somar')
    print('[2] Multiplicar')
    print('[3] Maior')
    print('[4] Novos Numeros')
    print('[5] Sair do programa')
    opt = int(input('Digite a opção: '))
    if opt == 1:
        soma = n + n1
        print(f'O resultado da soma é {soma}')
    if opt == 2:
        mult = n * n1
        print(f'O resultado da multiplicação é {mult}')

    if opt == 3:
        maior = max(n,n1)
        print(f'O maior número é {maior}')

    if opt == 4:
        n = int(input('Digite um numero:'))
        n1= int(input('Digite outro numero: '))




