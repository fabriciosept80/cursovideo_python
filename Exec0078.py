#Faça um programa que leia 5 valores numericos e guarde os em uma lista. No final mostre qual o maior e o menor
#valor digitados e indicando suas respectivas posições na lista.

numero = []
maior =  []
menor = []
for x in range (0,5):
    numero.append(int(input(f'Digite o {x+1}º número: ')))

for i, v in enumerate(numero):
    if v == max(numero):
        maior.append(i)
    if v == min(numero):
        menor.append(i)
maior_str = str(maior)[1:-1]
menor_str = str(menor)[1:-1]
print('Valores digitados foram: ',*numero)
print(f'O número {max(numero)} é o maior valor digitado e esta nas posições {maior_str}')
print(f'O número {min(numero)} é o menor valor digitado e esta nas posiçôes {menor_str}')
