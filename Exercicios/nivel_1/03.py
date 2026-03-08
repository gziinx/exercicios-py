# 3. Leia dois números e mostre qual é o maior (ou informe que são iguais).

numero = int(input("Escreva o seu numero:"))
numero1 = int(input("Escreva o seu segundo numero:"))

if numero > numero1:
    print ( numero, "é maior")
elif numero1 > numero:
    print (numero1, "é maior")
else:
    print ("os numeros são iguais")