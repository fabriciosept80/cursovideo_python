#Crie um programa que vai gerar 5 números aleatórios e colocar em um tupla.Depois disso, mostre a listagem de números
# gerados e também indique o menor e maior valor que estão na tupla.

from random import randint
n = (randint(1,50), randint(1,50), randint(1,50), randint(1,50), randint(1,50))
print(f'Os números sorteados foram:',end='')
for numeros in n:
    print(f'{numeros}',end=' ')
print()
print(f'O maior número da série é : {max(n)} e o menor é: {min(n)}')

