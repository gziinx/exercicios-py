# 2. Leia a idade de uma pessoa e classifique: criança (0–12), adolescente (13–17), adulto (18+). Se a idade for negativa, informe “idade inválida”.


numero = int(input("Escreva a sua idade:"))

if numero < 0:
    print("Idade inválida")
elif numero <= 12:
    print("Criança")
elif numero >= 13 and numero <= 17:
    print("Adolescente")
else:
    print("Adulto")