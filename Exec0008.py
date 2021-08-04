#Escreva um programa que leia um valor em metros e o exiba convertido em centimetro e militros.
numero = float(input("Entre com um valor em metros: "))
centimetros = numero * 100
milimetros = numero * 1000

print("O valor {:*^10} em metros equivale a {:*^10} centimetros e {:*^10} milimetros !".format(numero,centimetros,milimetros))
