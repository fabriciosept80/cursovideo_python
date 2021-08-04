#Faça um programa que leia o salario de um funcionario e mostre seu novo salario com 15% de aumento.

salario = float(input("Qual o salario do funcionário: "))
progressao = float(input("Entre com o aumento do salario do funcionario: "))
newsalario = salario + (salario *(progressao/100))
print("O salario de R$ {:.2f} do funcionário, passará a ser de R$ {:.2f} ".format(salario,newsalario))