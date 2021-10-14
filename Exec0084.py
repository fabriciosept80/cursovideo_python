#Faça um programa que leia nome e peso de varias pessoas, guardando tudo em um lista. No final, mostre :
#a) Qts pessoas foram cadastradas.
#b) Uma listagem com as pessoas mais pesadas.
#c) Uma listagem com as pessoas mais leves.

print("#"*30)
print('Cadastro de nomes e pesos'.center(30))
dados = list()
oficial = list()
leves = pesados = 0
while True:
    dados.append(str(input('Digite um nome: ')))
    dados.append(float(input('Digite o peso: ')))
    if len(oficial) == 0:
        leves = pesados = dados[1]
    else:
        if dados[1] < leves:
            leves = dados[1]
        if dados[1] > pesados:
            pesados = dados[1]
    oficial.append(dados[:])
    dados.clear()
    continuar = input('Deseja continuar [s/n]: ')
    if continuar in 'Nn':
        break
print()
for p in oficial:
    if p[1] == pesados:
        print(f'{p[0]} é a pessoa mais pesada com {pesados} kg')
    if p[1] == leves:
        print(f'{p[0]} é a pessoa mais leve com {leves} kg')
print('-'*30)
print(f'Foram cadastradas {len(oficial)} pessoas')






