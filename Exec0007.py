#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua media.
nome = input("Entre com o nome do aluno: ")
n1 = int(input("Entre com 1ª nota do aluno : "))
n2 = int(input("Entre com a 2ª nota do aluno: "))
media = (n1+n2)/2
print("O aluno(a) {:=^20} teve média : {:*^20} !".format(nome,media))