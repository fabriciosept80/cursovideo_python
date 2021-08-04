#Desenvolva um programa que leia o comprimento de 3 retas e diga ao usuário se elas podem ou não formar um triangulo.

r1 = int(input("Digite o valor da reta1: "))
r2 = int(input("Digite o valor da reta2: "))
r3 = int(input("Digite o valor da reta3: "))

if (abs(r2 - r1) < r1 and r1 < (r2 + r3)) or (abs(r1 - r3) < r2 and r2 < (r1 + r3)) or (abs(r1 - r2) < r3 and r3 < r1 + r2):
    print(f"Os valores {r1} e {r2} e {r3} podem formar um triangulo.")
else:
    print("Os valores não podem formar um triangulo.")

