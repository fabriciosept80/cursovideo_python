#Desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares. Se o valor
#digitado for impar , desconsidere-o.
lista = []
soma = 0
cont = 0
for x in range(0,6) :
    n = int(input(f"Digite o {x+1}º numero: "))
    lista.append(n)
    if lista[x] % 2 == 0:
        soma += lista[x]
        cont += 1
print(f'A soma dos {cont} pares digitados foi de {soma}.')