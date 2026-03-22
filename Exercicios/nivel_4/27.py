# 27. Leia uma sequência de números (quantidade N) e conte quantas vezes o valor 0 apareceu.
n = int(input('Digite um número: '))

for i in range (1, n):
    if i == 0:
        zero += 1
print(i , ' possui ', zero, 'zeros')