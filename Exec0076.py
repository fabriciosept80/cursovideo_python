#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequencia.
#No final, mostre uma listagem de preços organizando os dados em forma tabular.

nomeprodutos = ('Alface',1.50,'Banana',4.0,'Mandioca',2.99,'Laranja',1.50,'Mamão',3.50,'Couve',2.00,'Batata',2.0,'Cenoura',2.40,'Alho',6.30,'Rucula',4.50)
print('*'*40)
print(f'{"PREÇOS DA FEIRA":^40}')
print('*'*40)
for n in range(0,len(nomeprodutos)):
    if n % 2 == 0:
        print(f'{nomeprodutos[n]:.<30}',end=' ')
    else:
        print(f'R$ {nomeprodutos[n]:>5.2f}')
print('*'*40)

