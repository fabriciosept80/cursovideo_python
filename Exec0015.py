# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

print("="*70,"LOCADORA TABAJARA","="*65)
print(" ")
dias = int(input("Quantos dias o cliente ficou com o carro:"))
km = float(input("Qual a quilometragem percorrida pelo cliente: "))
total = (60 * dias) + (0.15 * km)
print('O cliente ficou com o carro {} dias e rodou {:.2f} kms, o saldo a pagar é de R$ {:.2f} '.format(dias,km,total))