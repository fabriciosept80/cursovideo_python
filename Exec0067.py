#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O
#programa será interrompido quando o número solicitado for negativo.
print("<>"*50)
print('\033[3;39;42mTABUADA\033[m'.center(120))
print("<>"*50)
while True:
    print('-'*40)
    n = int(input('Qual tabuada você deseja ?: '))
    print('-' * 40)
    if n < 0:
        print('\033[1;37m<<FIM DE PROGRAMA>>\033[m')
        break
    for valor in range (0,11):
        print(f'{valor} X {n} = {valor*n}')



