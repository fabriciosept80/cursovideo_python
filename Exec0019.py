#Um professor quer sortear um de seus 4 alunos para apagar o quadro. Faça um programa que ajude ele , lendo o nome
#deles e escrevendo o nome do escolhido.
import random

name = []
count = 1
print("")
while count <= 4:
    nome = input("Entre com o nome dos alunos: ")
    name.append(nome)
    count += 1
escolha = random.choice(name)
print(" ")
print("Dentre os seguintes nomes:",*name, sep = " - ")
print(f"O escolhido para apagar o quadro foi: {escolha}")
