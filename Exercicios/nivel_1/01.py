#1. Leia um número inteiro e informe se ele é positivo, negativo ou zero.

numero = int(input("Escreva o seu numero:"))

if numero > 0:
    print("seu numero é positivo")
elif numero == 0:
    print("Seu numero é igual a 0")
else:
    print("Seu numero é negativo")