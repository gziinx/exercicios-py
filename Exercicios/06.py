# 6. Leia o preço de um produto e aplique desconto: até 100 (5%), de 100.01 a 300 (10%), acima de 300 (15%). Mostre preço final.


numero = float(input("Escreva o preço do produto:"))
desconto_de_5 = numero * 5 / 100
desconto_de_10 = numero * 10 / 100
desconto_de_15 = numero * 15 / 100

if numero <= 100:
    numero = numero - desconto_de_5
    print("Seu preço ficou de", numero)
elif numero <= 300:
    numero = numero - desconto_de_10
    print("Seu preço ficou de", numero)
else:
    numero = numero - desconto_de_15
    print("Seu preço ficou de", numero)
