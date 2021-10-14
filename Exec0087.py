#Aprimore o desafio anterior (86), mostrando ao final:
#a) A soma de todos os valores pares digitados
#b) A soma dos valores da terceira coluna
#c) O maior valor da segunda linha
print('#'*30)
print('Estatísticas da matriz'.center(30))

somap = soma3 = 0
matrix = [[0,0,0],[0,0,0],[0,0,0]]
for l in range(0,3):
    for c in range (0,3):
        matrix[l][c] = int(input(f'Digite o valor para {l,c}: '))
print("_"*30)
for l in range(0,3):
    soma3 = soma3 + matrix[l][2]
    for c in range (0,3):
        print(f'[{matrix[l][c]:^5}]'.center(10),end='')

        if matrix[l][c] % 2 == 0:
            somap = somap + matrix [l][c]
    print()
mx = max(matrix[1])
print('*'*30)
print(f'A soma de todos os valores pares é {somap}')
print(f'A soma dos valores da 3ª coluna é {soma3}')
print(f'O maior valor da 2ª linha é {mx}')