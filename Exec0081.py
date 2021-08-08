#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
#a) Quantos números foram digitados
#b) A lista de valores ordenada de forma decrescente
#c) Se o valor 5 foi digitado e esta ou não na lista.

lista =[]
listanew = []
resp = 'S'
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    resp = str(input('Deseja digitar outro numero [S/N]: ')).upper().strip()
    if resp !='S':
      break
print(f"Foram digitados {len(lista)} elementos na lista")
lista.sort(reverse=True)
print(f'A lista invertida fica da seguinte forma {lista}')
print(f'A lista invertida fica da seguinte forma {lista.sort(reverse=True)}')
if 5 in lista:
    print("Existe o nº 5 na lista")
else:
    print("Não existe o nº 5")

