#Elabore um programa que calcule o valor a ser pago por um produto considerando o seu preço normal e condição de
#pagamento :
#A vista dinheiro/cheque : 10% desconto
#A vista no cartao : 5% desconto
#Em até 2x no cartao: preço normal
#3 x ou mais no cartão : 20% de juros.
print("")
print("◙"*50,"lojas calcinha preta".title(),"◙"*45) #{:=^40} para usar tb no lugar do"◙"*50
print("\033[1;36m_"*153,"\033[m")
def vista10(valor):
    total = valor - (valor * (0.1))
    print(f"O valor a ser pago será de R$ \033[7;33m{total:.2f}\033[m")
def vista5(valor):
    total = valor - (valor * (0.05))
    print(f"O valor a ser pago será de R$ \033[7;33m{total:.2f}\033[m")
def normal(valor):
    total = valor
    print(f"O valor a ser pago será de R$ \033[7;33m{total:.2f}\033[m")
def tree(valor):
    total = valor + (valor * (0.2))
    print(f"Sua compra será parcelada em 3x R${total/3:.2f}")
    print(f"O valor a ser pago será de R$ \033[7;33m{total:.2f}\033[m")

print("")
valor = float(input("Digite o valor da compra em R$: "))
modox = int(input("Digite o modo de pagamento: \033[1;36m1-Money or check\033[m || \033[1;35m2-Credit\033[m || \033[1;34m3-Two times in credit\033[m || \033[1;33m4-Tree times in credit\033[m: "))
if modox == 1:
    vista10(valor)
elif modox == 2:
    vista5(valor)
elif modox == 3:
    normal(valor)
elif modox == 4:
    tree(valor)
else:
    print("Opção errada, tente novamente !!")