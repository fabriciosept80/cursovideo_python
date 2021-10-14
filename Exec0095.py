#Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas
#partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em
#um dicionario, incluindo o total de gols feitos durante o campeonato.

#Aprimore o desafio 093 para que ele funcione com varios jogadores, incluindo um sistema de visualização de detalhes do
#aproveitamento de cada jogador.

print('▀'*70)
print('GESTÃO JOGADORES'.center(70))
print('▀'*70)
jogador = {'Nome':'',
           'Partidas':'',
           'Gols':'',
           'Total Gols':''}
ficha = list()
gol = list()

while True:
    count = 1
    jogador['Nome'] = str(input('Nome do jogador: ').upper())
    jogador['Partidas'] = int(input(f'Quantas partidas o jogador {jogador["Nome"]} jogou ?: '))
    while jogador['Partidas'] >= count:
        gol.append(int(input(f'Gols na {count}ª partida: ')))
        jogador['Gols'] = gol[:]
        jogador['Total Gols'] = sum(gol[:])
        count += 1
    ficha.append(jogador.copy())
    while True:
        resp = str(input('Deseja continuar [S/N]:').upper())
        if resp in 'SN':
            break
        print("Somente S ou N")
    if resp == 'S':
        gol.clear()
    if resp in 'N':
        gol.clear()
        break
print()
#print('Código',end='') # outra forma de fazer cabeçalho
#for z in jogador.keys(): # outra forma de fazer cabeçalho
#    print(f'{z:<15}',end='') # outra forma de fazer cabeçalho
print()
print(f'{"Codigo":<4}{"Nome":>10}{"Partidas":>18}{"Gols":>17}{"Total Gols":>20}') # mostrar resultados
print('▀'*70)# mostrar resultados
for k, v in enumerate(ficha,start=1):# mostrar resultados
    print(f'{k:>3} ',end='')# mostrar resultados
    for d in v.values():# mostrar resultados
        print(f'{str(d):^18}',end='')# mostrar resultados
    print('')# mostrar resultados
print('▀'*70)# mostrar resultados
#print(ficha[0]['Nome']) #testando o index do final do programa
while True:
    index = int(input('Qual jogador deseja saber mais informações [1000 para sair]: '))-1
    print()
    if index == 999:
        print('▀'*70)
        print('OBRIGADO POR USAR O SISTEMA'.center(70))
        print('▀' * 70)
        break
    if index >= len(ficha) :
        print(f"Não existe jogador cadastrado neste número {index+1}")
    else:
        print(f'Dados jogador {ficha[index]["Nome"]}: ')
        print('▀' * 70)
        for i, v in enumerate(ficha[index]['Gols']):#aqui ['Gols'] é uma lista.
            print(f'• No {i+1}º jogo {ficha[index]["Nome"]} fez  {v} gols'.center(70))
        print('▀'*70)




