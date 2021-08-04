#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos. Faça um programa
# que leia o nome dos alunos e mostre a ordem sorteada.

import random
count = 1
name = []
print("="*50,"Sorteio de nomes para apresentação do Trabalho","="*50)
print("")
while count <= 4:
    nome = input("Digite o nome do aluno : ")
    name.append(nome)
    count += 1
random.shuffle(name)
print("Nome dos alunos sorteados para apresentação dos trabalhos :""-",*name,"-")

