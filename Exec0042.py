#Refaça o desafio 35 dos triangulos acrescentando o recurso de mostrar que tipo de triangulo será formado.
#Equilatero : 3 lados iguais
#Isosceles : 2 lados iguais
#Escaleno : 3 lados diferentes
lados =[]
count = 1
print("")
print("calculo triangulo".upper().center(150))
print("")
while count <= 3:
    side = float(input(f"Digite o {count}º lado do triangulo: "))
    lados.append(side)
    count += 1
if lados[0] < lados[1] + lados[2] and lados[1] < lados[0] + lados[2] and lados[2] < lados[0] + lados[1]: #forma simplificada de verificar os lados do triangulo.

#if (abs(lados[1] - lados[0]) < lados[0] and lados[0] < (lados[1] + lados[2])) or (abs(lados[0] - lados[2]) < lados[1] and lados[1] < (lados[0] + lados[2])) or (abs(lados[0] - lados[1]) < lados[2] and lados[2] < (lados[0] + lados[1])):

    if lados[0] == lados[1] == lados[2]:
        print(f"Os lados {lados[0]} e {lados[1]} e {lados[2]} formam um triangulo \033[1;32mEQUILÁTERO\033[m")
    elif lados[0] != lados[1] != lados[2] != lados[0]:
        print(f"Os lados {lados[0]} e {lados[1]} e {lados[2]} formam um triangulo \033[1;33mESCALENO\033[m")
    else: #lados[0] == lados[1] and lados[2] != lados[1] or lados[0] == lados[2]: testar isosceles pior condição
       print(f"Os lados {lados[0]} e {lados[1]} e {lados[2]} formam um triangulo \033[1;31mISÓSCELES\033[m")
else:
    print(f"Os valores {lados[0]} e {lados[1]} e {lados[2]} não formam um \033[7;34mTRIÂNGULO\033[m")

