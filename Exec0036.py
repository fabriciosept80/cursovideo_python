#Escreva um programa para aprovar um emprestimo bancario para a compra de uma casa. O programa vai perguntar o valor
#da casa , o salario do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que
#ela não pode exceder 30% do salário, ou então o emprestimo será negado.

cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m',
         'verde': '\033[1;32m',
         'vermelho':'\033[7;31m'}
print("")
print(cores['azul'],"$"*60,cores['limpa'],cores['amarelo'],
      "EMPRÉSTIMO IMOBILIÁRIO",cores['limpa'],cores['azul'],"$"*60,cores['limpa'])
print("")
v_casa = float(input("Qual o valor do imóvel em R$: "))
v_salario = float(input("Qual o salário mensal em R$: "))
v_anos = float(input("Quantos anos vai fazer o financiamento: "))
meses = v_anos * 12
prest = v_casa / meses
if prest > (0.3 * v_salario):
    print("O valor da prestação será de: ",cores['vermelho'],f'R$ {prest:.2f}',cores['limpa'])
    print(f"\033[7;31mNÃO PODE FAZER FINANCIAMENTO\033[m,R$ {v_salario:.2f} mensal, compromete 30% renda!")
    print(cores['verde'],"*-TENTE UM TEMPO MAIOR ou RENDA MAIOR-*",cores['limpa'])
elif prest <= (0.3 * v_salario):
    print("O valor da prestação será de: ",cores['azul'],f'R$ {prest:.2f}',cores['limpa'])
    print(cores['azul'],'*FINANCIAMENTO APROVADO*',cores['limpa'])
print(cores['amarelo'],"#"*60,' TENHA UM BOM DIA ! ',"#"*60,cores['limpa'])
