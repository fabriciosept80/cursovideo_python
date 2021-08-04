#Crie um programa que tenha um tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa
#deverá ler um número pelo teclado (entre 0 e 20) e mostra-lo por extenso.

nomenumero = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

nposition = int(input('Digite um número : '))
while nposition < 0 or nposition >20:

    nposition = int(input('Digite um número : '))
print(f'Você digitou o número: {nomenumero[nposition]}.')
