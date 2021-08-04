#Crie um algoritmo que leia um número e mostre o seu dobro,triplo e raiz quadrada
number = int(input("Entre com um número: "))
dobro = 2 * number
triplo = 3 * number
raiz = number ** (1/2)
print("O dobro do numero {} é {} o seu triplo é {} e a sua raiz quadrada é {:.2f}!".format(number, dobro, triplo, raiz))