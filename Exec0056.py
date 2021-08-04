#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do
# grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
nomeVelho = ''
homemVelho = 0
soma = 0
somaM = 0
for x in range(1,5):
    print(f'Cadastro {x}')
    nome = str(input(f'Digite o nome da {x}ª pessoa: ')).strip().upper()
    idade = int(input(f'Digite a idade da {x}ª pessoa: '))
    soma += idade
    media = soma / x
    sexo = str(input(f'Digite o sexo da {x}ª pessoa, M ou F: ')).strip().upper()
    if x == 1 and sexo =="M":
        homemVelho = idade
        nomeVelho = nome
    if idade >= homemVelho and sexo == "M":
        homemVelho = idade
        nomeVelho = nome
    if idade < 20 and sexo == "F":
        somaM += 1
print(f'A media de idade do grupo é de {media}')
print(f'O Sr.{nomeVelho} é a pessoa mais velha do grupo, com {homemVelho} anos.')
print('O total de mulheres com menos de 20 é {}'.format(somaM))
