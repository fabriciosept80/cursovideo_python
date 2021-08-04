#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e quantos dolares ela pode comprar. Dolar = 3,27
real = float(input("Quanto dinheiro o cliente tem na carteira : "))
dolar = float(input("Entre com o valor do dólar no dia: "))
dolarcalc = real / dolar
print("Com {:*^20} reais na carteira é possivel comprar {:*^20.2f} doláres.".format(real,dolarcalc))