#Faça um programa que calcule a soma entre todos os numeros impares que são multiplos de 3 e que se encontram no
#intervalo de 1 até 500
soma = 0
cont = 0
for x in range (1,501,2):
    if x % 3 == 0:
        cont += 1
        soma += x

print('')
print(f'A soma de todos os números impares multiplos de 3 é {soma} - {cont}')

