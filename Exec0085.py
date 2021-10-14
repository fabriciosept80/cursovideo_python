#85 - Crie um programa onde o usuario possa digitar sete valores numericos e cadastre-os em uma lista unica que
#mantenha separado os valores pares e impares. No final, mostre os valores pares e impares em ordem crescente.
print('*'*30)
print('Números Pares e Impares'.center(30))
numeros = list()
par = list()
impar = list()
numfinal = []
for a in range(1,8):
    numeros.append(int(input(f'Digite o {a}º número: ')))
for x in numeros:
    if x % 2 == 0:
        par.append(x)
        par.sort()
    elif x % 2 == 1:
        impar.append(x)
        impar.sort()
numeros.clear()
numfinal.append(par[:])
numfinal.append(impar[:])
print(f'Numeros pares {numfinal[0]} e numeros impares {numfinal[1]}')

