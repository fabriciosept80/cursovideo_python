#Faça um programa que leia 3 números e diga qual é o maior e qual é o menor.

n1 = float(input("Digite um número qualquer: "))
n2 = float(input("Digite um número qualquer: "))
n3 = float(input("Digite um número qualquer: "))
# poderia admitir que alguem é maior ou menor:
# maior = a ou menor = a
# dai colocaria:
#if n2>n3 and n2>n1
#    maior = n2
if n1 > n2 and n1 > n3 and n2 > n3:
    print(f'O {n1} é maior que o {n2} que é maior que o {n3}.')
elif n2 > n1 and n2 > n3 and n1 > n3:
    print(f'O {n2} é maior que o {n1} que é maior que o {n3}.')
elif n3 > n1 and n3 > n2 and n1 > n2:
    print(f'O {n3} é maior que o {n1} que é maior que o {n2}.')
elif n3 > n1 and n3 > n2 and n2 > n1:
    print(f'O {n3} é maior que o {n2} que é maior que o {n1}.')
elif n2 > n1 and n2 > n3 and n3 > n1:
    print(f'O {n2} é maior que o {n3} que é maior que o {n1}.')
elif n1 > n2 and n1 > n3 and n3 > n2:
    print(f'O {n1} é maior que o {n3} que é maior que o {n2}.')
