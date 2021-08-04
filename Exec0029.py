#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80 km/h, mostre uma mensagem dizendo que ele
#foi multado. A multa vai custar R$ 7,00 por cada km acima do limite.
allow = 80
multa = 7
vel = float(input("Digite a velocidade do carro em km/h: "))
if vel > 80:
    print(f'Velocidade atual {vel} km/h')
    print(f'Você excedeu o limite de velocidade em {vel - allow} km/h - MULTADO')
    print(f'Você foi multado em R$ {(vel - allow )* multa:.2f} ')
else :
    print(f"Você esta dentro do limite de velocidade 80 km/h. Parabéns !!")
    print(f'Velocidade atual {vel} km/h.')
print('Tenha um bom dia !!')