#Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas
#partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em
#um dicionario, incluindo o total de gols feitos durante o campeonato.

count = 1
gol = []
player = {'Nome':'','Partidas':'','Gols':'','Total Gols':''}
print('*'*35)
print('CAMPEONATÃO AMADORZINHO'.center(35))
player['Nome'] = str(input('Digite nome do jogador: ').upper())
player['Partidas'] = int(input(f'Digite a quantidade de partidas de {player["Nome"]}: '))
while count <= player['Partidas']:
    gol.append(int(input(f'Digite a quantidade de gols na {count}ª partida: ')))
    player['Gols']=gol[:]
    count +=1
player['Total Gols'] = sum(gol)
print('*'*35)
print('RESUMO'.center(35))
for k, v in player.items():
    print(f'O campo {k} tem o valor {v}.')
print('*'*35)
print('ARTILHEIRO'.center(35))
print(f'O jogador {player["Nome"]} fez {player["Partidas"]} partidas')
#for i, v in enumerate(gol):
for i, v in enumerate(player['Gols']): # fazendo enumerate em uma parte do dicionario.!!!
    print(f' ==> Na partida {i+1} ele fez {v} gols')
print(f'Foi um total de {sum(gol)} gols !!!')
