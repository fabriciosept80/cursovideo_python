#Refaça o desafio 51 , lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
#usando a estrutura while.
firstTerm = int(input('Digite o 1º termo: '))
razao = int(input('Digite a razão: '))
cont = 8
numero=[]
numero.append(firstTerm)
while cont >= 0 :
    firstTerm = firstTerm + razao
    cont -= 1
    numero.append(firstTerm)
print(*numero,sep='-')



