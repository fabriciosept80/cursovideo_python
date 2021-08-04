#Crie um programa que leia varios números inteiros pelo teclado. O programa só vai parar quando o usuario digitar
#o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre
#eles (desconsiderando o 999)
n = count = soma = 0

print('\033[1;36m<<< PARA SAIR DIGITE 999 >>>\033[m')
n = int(input('Digite um número inteiro qualquer: '))
while n != 999:
    soma += n
    count +=1
    n = int(input('Digite um número inteiro qualquer: '))
print(f'{count} total de números digitados')
print(f'{soma} valor da soma de todos os números digitados')