#Melhore o desafio 61, perguntando para o usuario se ele quer mostrar mais alguns termos. O programa encerra quando
#ele disser que quer mostrar 0 termos.

n=int(input('Digite o 1º termo: '))
razao=int(input('Digite a razão: '))
cont = 8
numero=[]
numero.append(n)
while cont >=0:
    n = n + razao
    cont -= 1
    numero.append(n)
print(*numero)
opt = str(input('Você deseja mostrar mais alguns termos [s/n]: ')).strip().upper()

while opt == 'S':
    newterm = int(input('Quantos termos voce quer continuar? : '))

    if newterm != 0:
        cont = newterm - 1
        while cont >= 0:
            n = n + razao
            cont -= 1
            numero.append(n)
        print(*numero)
        opt = str(input('Você deseja mostrar mais alguns termos [s/n]: ')).strip().upper()
    else:
        print('Foram exibidos {} termos'.format(len(numero)))
        print('\033[2;31mFIM DO PROGRAMA\033[m')
        break
else:
    print('Foram exibidos {} termos'.format(len(numero)))
    print('\033[2;31mFIM DO PROGRAMA\033[m')








