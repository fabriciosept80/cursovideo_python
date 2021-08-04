#Faça um programa que leia um numero inteiro e diga se ele é primo ou não.
soma=0
n=int(input('Digite um numero inteiro: '))
for x in range (1,n+1):
    if n % x == 0:
        #print(f'{x}',end=' ')
        soma += 1
if soma == 2 :
    print(f"\nO número {n} é primo.")
else:
    print(f'\nO número {n} não é primo !')
