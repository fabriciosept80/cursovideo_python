#Crie um programa que tenha uma tupla com varias palavras. Depois disso, vc deve mostrar para cada palavra quais são
#as suas vogais.

palavras = ('onibus','cafe','diamante','cachorro','gato','televisao','GATO','fAbrIcIO','Livia','zenith')

for n in palavras:
    print(f'\nA palavra {n} tem as vogais:',end=' ')
    for vogal in n:
        if  vogal.lower() in 'aeiou' :
          print(vogal,end=' ')
