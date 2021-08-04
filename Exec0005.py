#Faça um programa que leia um número inteiro e mostre na tela o sucesso e seu antecessor.
numero = int(input("Entre com um numero: "))
nbefore = numero - 1
nafter = numero + 1
print("O número anterior a {} é {} e o posterior é {}!".format(numero,nbefore,nafter))