#Refaça o desafio 09 , mostrando a tabuada de um numero que o usuario escolher, utilizando o laço for:

print('#'*65,'TABUADA MULTIPLICAÇÃO','#'*65)
n=int(input('De qual número vc quer a tabuada : '))
for x in range(0,11):
    multi = n * x
    print(n,'*',x,'=',multi)
