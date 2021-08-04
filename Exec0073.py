#Crie um tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro , na ordem de colocação.
#Later, you must show:
#a) Only five first places
#b) Last four places in the table.
#c) A list with the teams in alphabetical order
#d) What's the position is Chapecoense Team in Table ?
print('<>'*45)
tabela = ('Palmeiras','Atlético-MG','Fortaleza','Bragantino','Athletico-PR','Flamengo','Ceará','Atlético-GO','Bahia','Fluminense','Santos','Internacional','Juventude','Cuiabá','Sport','São Paulo','América-MG','Grêmio','Corinthians','Chapecoense')
print('<>'*45)
print(tabela)
print('<>'*45)
print(f'Os primeiros 5 colocados são: {tabela[0:5]}')
print('<>'*45)
print(f'Os ultimos 4 colocados são: {tabela[-4:]}')
print('<>'*45)
print(f'Os times em ordem alfabética são: {sorted(tabela)}')
print('<>'*45)
n= tabela.index('Chapecoense')
print(f'O time da Chapecoense esta na posição {(n+1)}')

