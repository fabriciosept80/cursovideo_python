#Faça um programa que verifique se o nome da cidade começa com SANTO.
cidade = str(input("Digite o nome da cidade: ")).strip()
cidade = cidade.upper()
if cidade.split()[0] == "SANTO":
    print(f"O nome da cidade {cidade} começa com {cidade.split()[0]}")
else:
    pass
