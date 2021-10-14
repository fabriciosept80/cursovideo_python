#Faça um programa que leia nome é media de um aluno guardando também a situação em um dicionario. No final, mostre o
#conteúdo da estrutura na tela.

dados = {}
print('*'*40)
print('Exemplo Boletim com Dicionario'.center(40))
print()
dados['nome'] = str(input("Digite o nome do aluno : ").upper())
dados['media'] = float(input("Digite a média do aluno: "))
if dados['media'] >= 7:
    dados['status'] = 'APROVADO'
else:
    dados['status'] = 'REPROVADO'
print(f'Nome é igual a {dados["nome"]}')
print(f'Média é igual a {dados["media"]}')
print(f'A situação é igual a {dados["status"]}')
print('#'*60)
print('Ou também posso apresentar assim : ')
for k, v in dados.items():
    print(f'{k}:{v}')