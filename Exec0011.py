#Faça um programa que leia a largura e altura de uma parede em metros, calcule sua área e a quantidade de tinta para
# pinta-la, sabendo que cada litro de tinta, pinta uma área de 2m².
print('='*60,"CALCULO DE TINTA",'='*60)
print(" ")
altura = float(input("Entre com altura da parede: "))
largura = float(input("Entre com a largura da parede: "))
area = altura * largura
consumo = area / 2
print("A área da parede é de {:*^15.2f} metros² e o total de tinta para pinta-la será de {:*^.2f} litros".format(area,consumo))
