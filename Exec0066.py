#Crie um programa que leia vários números inteiros pelo teclado . O programa só vai parar quando o usuário digitar
#o valor de 999, que é a condição de parada. No final mostre quantos números foram digitados e qual foi a soma entre
#eles (desconsiderando o flag)

cont = soma = n = 0
while True:
    n = int(input('Digite um numero inteiro - [999 > parar]:  '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'Você digitou {cont} números e a soma entre eles é de {soma}.')
