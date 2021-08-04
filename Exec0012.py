#Faça um algoritmo que leia o preço de um produto e mostre o seu novo preço com 5% de desconto.

preco = float(input("Digite o preço do produto: "))
desconto = float(input("Digite o desconto a ser aplicado: "))
newpreco = ((preco *(desconto/100)) - preco) * -1
print("O valor do produto de R$ {:.2f} com aplicação do desconto de {:.2f}% terá o novo preço de: R$ {:.2f} .".format(preco,desconto,newpreco))