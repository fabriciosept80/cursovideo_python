#Crie um programa que vai ler vários números e colocar em um lista. Depois disso, crie 2 listas extras que vão conter
#apenas os valores pares e os valore impares digitados, respectivamente. No final, mostre o conteudo das 3 listas
#geradas
lista=[]
listap=[]
listai=[]
resp = 'S'
print()
while True:
    n= int(input('Digite um número: '))
    lista.append(n)
    resp = str(input('Deseja continuar [S/N]: ')).strip().upper()
    if resp != 'S':
        break
for a in lista:
    if a % 2 == 0:
        listap.append(a)
    else:
        listai.append(a)
print(f'Lista Geral: {lista}')
print(f'Lista Par: {listap}')
print(f'Lista Impar: {listai}')
