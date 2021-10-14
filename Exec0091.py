#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um
#dicionario. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior numero no dado.

from random import randint
from time import sleep
from operator import itemgetter

jogo = {'Player 1':randint(1,6),
        'Player 2':randint(1,6),
        'Player 3':randint(1,6),
        'Player 4':randint(1,6)}
ranking = list() # criada essa lista para salvar o valor do sorted, que vai posicionar os valores de acordo com o parametro
#selecionado no itemgetter.
print('Valores sorteados :')
for k, v in jogo.items():
    print(f'{k} tirou: {v} no dado')
    sleep(1)
ranking = sorted(jogo.items(),key=itemgetter(1),reverse=True) # IMPORTANTE ESSA LINHA, itemgetter pega o valor da
#indicado no parenteses.
print('*'*30)
print('RESULTADOS'.center(30))
for i, v in enumerate(ranking): #aqui vou tratar o resultado de ranking como lista
    print(f'  {i+1}º lugar: {v[0]} com {v[1]} ')# tupla dentro de lista posso usar v[0],v[1] e assim por diante.
    sleep(1)