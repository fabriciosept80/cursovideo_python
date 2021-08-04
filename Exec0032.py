#  Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO ou não.
from datetime import date # para usar datas
year = int(input("Entre com um ano qualquer. Se quiser o ano atual ditite 0: "))
if year ==0:
    year = date.today().year # pegando a data atual do sistema. Biblioteca datetime.

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 :
    print(f'O ano {year} é BISSEXTO')
else:
    print(f'O ano {year} NÃO É BISSEXTO')
