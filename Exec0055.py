#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

valor = []
for x in range (1,6):
    peso = float(input(f'Entre com o peso da {x}ª pessoa: '))
    valor.append(peso)
maior = max(valor);menor = min(valor)
print(f'O maior peso foi de {maior}kg e o menor peso foi de {menor}kg')