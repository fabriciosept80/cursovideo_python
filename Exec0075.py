#Develop a program which read four values by the keyboard and save them  in a tuple. In the end, show:
#a) How many times the number nine showed.
#b) In what position was typed the first number three.
#c) What was the pairs numbers

n = (int(input('Digite 1º número : ')),
     int(input('Digite 2º número : ')),
     int(input('Digite 3º número : ')),
     int(input('Digite 4º número : ')))
print('*'*40)
print(f'A tupla digitada foi: {n}')
print('*'*40)
print(f'O número *9* foi exibido: {n.count(9)} vezes')
if 3 in n:
    print(f'O número *3* aparece na posição: {n.index(3)+1}')
else:
    print('O valor *3* não esta presente na tupla')
print('Segue os valores pares digitados: ',end='')
for par in n:
    if par % 2 == 0:
        print(par,end=' ')
print(' ')
