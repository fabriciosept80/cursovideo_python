#Crie um programa que leia nome, sexo e idade de varias pessoas, guardando os dados de cada pessoa em um dicionario
# e todos os dicionarios em uma lista. No final mostre:
#a)Quantas pessoas foram cadastradas
#b)A media de idade do grupo
#c)Uma lista com todas as mulheres
#d)Uma lista com todas as pessoas acima da media.
from operator import itemgetter
dados = {'Nome':'',
         'Sexo':'',
         'Idade':''}
ficha = []
somaidade = 0
while True:
    dados.clear()
    dados['Nome']=str(input('Entre com nome: ').upper())
    while True:
        dados['Sexo'] = str(input('Entre com o sexo [M/F]: ').upper())
        if dados['Sexo'] in 'MF':
            break
        print('Digite somente M ou F')
    dados['Idade']=int(input('Entre com a idade: '))
    ficha.append(dados.copy())
    somaidade = somaidade + dados['Idade']
    media = somaidade/len(ficha)
    while True:
        resp = str(input('Deseja continuar ? [S/N]: ').upper())
        if resp in 'SN':
            break
        print('Digite somente S ou N')
    if resp == 'N':
        break

print(f'A) Há no cadastro {len(ficha)} pessoas')
print(f'B) A média de idade no grupo é de {media:3.2f} anos')
print(f'C) Lista de mulheres cadastradas :',end=' ')
for p in ficha:
    if p['Sexo'] == 'F':
        print(f'{p["Nome"]}',end=' ') #imprimir nomes onde sexo = f
print()#print vazio para quebra de linha
print(f'D) Pessoas com idade acima da media:', end=' ')
for x in ficha:
    if x['Idade'] >= media:
        print()
        #print(f'{x["Nome"]}',end=' ')
        for k, v in x.items():
            print(f'{k} = {v};',end=' ')
        print()
print('#'*40)
print('<FIM>'.center(40))
