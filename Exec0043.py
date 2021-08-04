#Desenvolva um lógica que leia o peso e altura de uma pessoa , calcule seu imc e mostre seu status , de acordo com os
#valores abaixo:
#Abaixo de 18.5: Abaixo do peso
#Entre 18.5 e 25: Peso ideal
#25 até 30 : Sobrepeso
#30 a 40 : Obsidade
#Acima de 40 : Obsidade mórbida.
print("\033[1;34m-"*160,"\033[m")
print("cálculo de imc".title().center(160))
print("\033[1;34m-"*160,"\033[m")
altura = (float(input("Digite sua altura: ")))
peso = (float(input("Digite seu peso: ")))
imc = peso/pow(altura,2)
print(f'{imc:.1f}')

if imc <= 18.5:
    print("Abaixo do peso")
elif imc > 18.6 and imc <= 25:
    print("Peso ideal")
elif imc > 26 and imc <= 30:
    print("Sobrepeso")
elif imc > 31 and imc <= 40:
    print("Obsidade")
elif imc >41:
    print("Obsidade Morbida")
