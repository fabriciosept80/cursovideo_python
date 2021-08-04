# Faça um programa que leia um número inteiro na tela e mostre sua tabuada.
numero = int(input("Entre com um número para calculo da tabuada: "))
count = 0
while count <= 10:
    totalmult = count * numero
    print(f"{count:2} * {numero:2} = {totalmult} ")
    count += 1
