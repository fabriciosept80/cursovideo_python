#Escreva um programa que pergunte o salário de um funcionário e calcule o valor de seu aumento. Para salários superiores
#a R$ 1250.00, calcule um aumento de 10 %. Para os inferiores ou iguais o aumento é de 15%.

step1 = 0.15
step2 = 0.1
sal_base = 1250
sal = float(input("Digite o salário em R$ do funcionário: "))
if sal >= sal_base:
    print(f'O salário do funcionário passará de R$ {sal} para R$ {(sal * step2) + sal}.')
else:
    print(f'O salário do funcionário passará de R$ {sal} para R$ {(sal * step1) + sal}.')
    