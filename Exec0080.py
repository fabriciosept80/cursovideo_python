#Crie um programa onde o usuário possa digitar 5 valores númericos e cadastre-os em uma posição da lista, já na
#posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

lista=[]
for x in range(0,5):
    n = int(input('Digite um número: '))
    if x == 0:
        lista.append(n)
    elif x > lista[len(lista) - 1]: # ou lista[-1]
        lista.append(n) # a saida é igual, posso colocar "or" no primeiro if.
    else:
        a = 0
        while a < len(lista):
            if n <= lista[a]:
                lista.insert(a,n)
                break
            a += 1
print(lista)