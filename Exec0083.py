#Crie um programa onde o usuário digite uma expressão qualquer que use parenteses. Seu aplicativo deverá analisar
#se a expressão passada está com os parenteses abertos e fechados na ordem correta.

lista =[]
countab = countfe = 0
exp = str(input('Digite uma expresão matemática: '))
for a in exp:
    lista.append(a)
print(lista)
for k in enumerate(lista):
    if "(" in k:
        countab += 1
    if ")" in k:
        countfe += 1
if countab == countfe:
    print("A expressão esta balanceada")
else:
    print("A expressão não esta balanceada")




