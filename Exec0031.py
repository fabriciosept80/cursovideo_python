#Desenvolva um programa que pergunte a distancia de uma viagem em km. Calcule o preço da passagem, cobrando R$0,50 por
#km para viagens de até 200km e R$ 0,45 para viagens mais longas.
band1 = 0.5
band2 = 0.45

dist = float(input("Digite a distancia da viagem em km: "))
preco = dist * 0.5 if dist <= 200 else dist * 0.45 #operador ternario = if simplificado. Outra forma de if
print("O valor da viagem será de R$ {:.2f}".format(preco))
if dist <= 200:
    print(f'O valor da viagem para {dist} km será de R$ {dist * band1:.2f}.')
else:
    print(f'O valor da viagem para {dist} km será de R$ {dist * band2:.2f} ')
