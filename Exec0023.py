#Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um de seus dígitos separadores
#ex : Digite um numero : 1834
#unidade : 4
#dezena : 3
#centena : 8
#milhar : 1
number =[]
numero = str(input("Digite um numero: "))

if len(numero) == 1:
    print(f"O numero {numero} tem {numero.strip()[0]} unidades")
elif len(numero) == 2:
    print(f"O numero {numero} tem {numero.strip()[1]} unidades")
    print(f"O numero {numero} tem {numero.strip()[0]} dezenas")
elif len(numero) == 3:
    print(f"O numero {numero} tem {numero.strip()[2]} unidades")
    print(f"O numero {numero} tem {numero.strip()[1]} dezenas")
    print(f"O numero {numero} tem {numero.strip()[0]} centenas")
elif len(numero) == 4:
    print(f"O numero {numero} tem {numero.strip()[3]} unidades")
    print(f"O numero {numero} tem {numero.strip()[2]} dezenas")
    print(f"O numero {numero} tem {numero.strip()[1]} centenas")
    print(f"O numero {numero} tem {numero.strip()[0]} milhares")

#Poderia ter feito usando modulo
# unidade = n // 1 % 10
# dezena = n // 10 % 10
# centena = n // 100 % 10
# milhar = n // 1000 % 10