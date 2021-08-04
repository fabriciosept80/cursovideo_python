#Crie um programa que leia uma frase qualquer e diga se ela é um palindromo , desconsiderando os espaços.

frase = str(input('Digite uma frase: ')).strip().upper()
frase_nova = frase.replace(" ","")
frase_invertida = ''
for x in range(len(frase_nova) - 1,-1,-1):
   frase_invertida += frase_nova[x]
if frase_nova == frase_invertida:
    print(f'\nA frase {frase_nova} é um palindromo, {frase_invertida}')
else:
    print(f'\nA frase {frase_nova} não é um palindromo, {frase_invertida}')










