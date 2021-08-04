#Escreva um programa que leia um numero n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequencia
#de Fibonnaci.
print('#'*40)
print('\033[1;35mSEQUENCIA FIBONACCI\033[m'.center(50))
print('#'*40)
cont = 3
n = int(input('Digite a quantidade de termos desejada: '))
n1 = 0
n2 = 1
n3 = 0
print(f'{n1} > {n2}', end='')
while cont <= n:
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    cont += 1
    print(f' > {n3}',end='')
print('')
print("="*cont*(5))

