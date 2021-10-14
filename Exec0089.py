#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final mostre um
# boletim, contendo a média de cada um  e permita que o usuario possa mostrar as notas de cada aluno individualmente.

dados = list()
aluno = list()
print('=-'*10,'BOLETIM TABAJARA','-='*10)
print()
while True:
    nome = str(input('Digite nome do aluno: ')).upper()
    dados.append(nome)
    n1 = float(input('Digite a 1ª nota: '))
    dados.append(n1)
    n2 = float(input('Digite a 2ª nota: '))
    dados.append(n2)
    media = ((n1+n2)/2)
    dados.append(media)
    aluno.append(dados[:])
    dados.clear()
    continuar = str(input('Deseja continuar [S/N]?: '))
    if continuar not in 'Ss':
        break
print('Média dos alunos')
print('-'*30)
print(f'{"Nº":<4}{"Aluno":<10}{"Média":>8}')
print('-'*30)
for i, j in enumerate(aluno,start=1):
    print(f'{i:<4}{j[0]:<10}{j[3]:>8.1f}')
    print('-'*30)
deseja = str(input('Deseja saber as notas individuais [S/N]: '))
if deseja in 'Ss':
    while True:
        indice = int(input('Digite o codigo do aluno: '))
        print()
        if indice <= len(aluno):
            print("Notas Aluno/Semestre")
            print()
            print(f'{"Nº":<4}{"Aluno":<10}{"1º Semestre":>13}{"2º Semestre":>15}')
            print('='*45)
            print(f'{indice:<4}{aluno[indice-1][0]:<10}{aluno[indice-1][1]:>13}{aluno[indice-1][2]:>16}')
            print('='*45)
            denovo = str(input('Deseja continuar [S/N] ?: '))
            if denovo not in 'Ss':
                print('Obrigado por usar o sistema')
                break
        else:
            print(f'Aluno não encontrado. Registros disponívies {len(aluno)}')
else:
    print('*'*30)
    print('Obrigado por usar o sistema'.center(30))

