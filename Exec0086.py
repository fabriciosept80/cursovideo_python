#Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a
#matriz na tela, com a formatação correta.

line = [[0,0,0],[0,0,0],[0,0,0]]

for l in range(0,3):
    for c in range (0,3):
        line[l][c] = int(input(f'Digite um número para posição {l,c}: '))
for l in range(0,3):
    for c in range(0,3):
        print(f'[{line[l][c]:^5}]'.center(2),end='')
    print()

