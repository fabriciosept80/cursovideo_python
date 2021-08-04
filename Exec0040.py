#Crie um programa que leia 2 notas de um aluno e calcule sua media, mostrando uma mensagem no final , de
#acordo com a média atingida.
#Media abaixo de 5.0 : REPROVADO
#Media entre 5.0 e 6.9: RECUPERAÇÃO
#Media acima de 7.0: APROVADO
import numpy as np
notas = []
count = 1
print("")
print("*"*70,"\033[1;36mBOLETIM ESCOLAR\033[m","*"*65)
print("")
while count <= 2:
    b = float(input(f"Digite a nota do {count}º Bimestre: "))
    notas.append(b)
    count += 1
if np.mean(notas) < 5:
    print(f"A sua média foi de {np.mean(notas):.2f}, você está \033[1;31mREPROVADO!\033[m")
elif np.mean(notas) > 5 and np.mean(notas) < 6.9:
    print(f"A sua média foi de {np.mean(notas):.2f}, você está de \033[1;33mRECUPERAÇÃO!!\033[m")
elif np.mean(notas) > 7:
    print(f"A sua media foi de {np.mean(notas):.2f}, você está \033[1;36mAPROVADO!!!\033[m")


