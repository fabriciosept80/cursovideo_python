#Crie um programa que leia varios numeros inteiros pelo teclado. No final da execução, mostre a media entre todos os
#valores e qual foi o maior e o menor valor lido. O programa deve perguntar ao usuario se ele quer ou não continuar a
#digitar os valores.

import statistics

valores =[]
media = 0;maximo = 0; minimo = 0
print('*'*50)
print('')
n = int(input('Digite um número inteiro qualquer: '))
valores.append(n)
c = str(input('Deseja contiunuar? [S/N] : ')).upper().strip()
while c == 'S':
    n = int(input('Digite um número inteiro qualquer: '))
    valores.append(n)
    c = str(input('Deseja contiunuar? [S/N] : ')).upper().strip()
    if c == 'N':
        media = statistics.mean(valores)
        maximo = max(valores)
        minimo = min(valores)
        break

print(f'A média dos valores digitados foi de \033[1;36m{media:.2f}\033[m')
print(f'O maior valor lido foi de \033[1;34m{maximo}\033[m')
print(f'O menor valor lido foi de \033[1;35m{minimo}\033[m')
