# 11. Leia 5 números inteiros e mostre quantos são pares e quantos são ímpares.

n = [1,2,3,4,5]
for i in n:
    if i % 2 != 0:
        print(i,"é impar")
    else:
        print(i,"é par")