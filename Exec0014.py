#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

print("*"*60,'CONVERSÃO DE TEMPERATURAS',"*"*60)
print(" ")
opt1 = int(input("Digite 1 para converter de Celsius para Fahrenheit ou 2 de Fahrenheit para Celsius: "))

if opt1 == 1:
   C = float(input("Digite a temperatura em Celsius: "))
   fhn = ((C * 1.8)  + 32)
   print(f"A temperatura em Fahrenheit é de : {fhn:.2f}F")

elif opt1 == 2 :
   F = float(input("Digite a temperatura em Fahrenheit: "))
   cel = ((F-32) / 1.8)
   print(f"A temperatura em Celsius é de : {cel:.2f}C" )







