#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionario
#se por acaso a CTPS for diferente de ZERO, o dicionario receberá  também o ano de contratação e o salario. Calcule e
#acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import date
print('*'*40)
print('Mal Aposentado - INSS'.center(40))
print()
dados = {'Nome':'','Data Nascimento':'','CTPS':'','IDADE':'','Ano Contratação':'','Salario Contratação':'','Idade Aposentadoria':''}

dados['Nome']=str(input('Digite nome: ')).upper()
dados['Data Nascimento'] = int(input('Digite ano nascimento: '))
dados['CTPS'] = int(input('Digite nº CTPS [0 SE NÃO TIVER]: '))
dados['IDADE'] = date.today().year - dados['Data Nascimento']
if dados['CTPS'] != 0:
    dados['Ano Contratação'] = int(input('Digite ano contratação: '))
    dados['Salario Contratação'] = float(input(f'Digite o salario:R$ '))
    idade_contrato = date.today().year - dados['Ano Contratação']
    dados['Idade Aposentadoria'] = idade_contrato + 35
    print('*'*40)
    print('RESUMO')
    print()
    for k, c in dados.items():
        print(f'{k} : {c}')
else:
    print('*'*40)
    print('RESUMO')
    print()
    print(f'Nome:{dados["Nome"]}')
    print(f'Idade:{dados["IDADE"]}')
    print(f'CTPS:{dados["CTPS"]}')
