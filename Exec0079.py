#Crie um programa onde o usuário possa digitar vários valores númericos e cadastre - os em uma lista. Caso o número já
#exista la dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem
#crescente.

lista = []
print()
print('#'*40)
print('\033[1;34mTESTE DE LISTA\033[m'.center(50))
print('#'*40)
print("ENTRE COM 10 NÚMEROS")

for x in range(1,10):
    num=int(input("Digite um numero: "))
    if num in lista:
        lista.remove(num)
    lista.append(num)
    lista.sort()
print(f'Os número digitados foram: {lista}')
