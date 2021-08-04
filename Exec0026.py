#Faça um programa que leia uma frase pelo teclado  e mostre :]
#Quantas vezes aparece a letra "A"
#Em que posição ela aparece a 1ª vez
#Em que posição ela aparece a ultima vez.

frase = input("Digite uma frase: ").strip()
frase = frase.upper()
print(f"Na frase {frase} a letra A aparece {frase.count('A')} vezes.")
print(f"Na frase {frase} a primeira letra A aparece na posição {frase.find('A')}")
print(f"Na frase {frase} a última letra A aparece na posição {frase.rfind('A')}")
