# 27. Leia uma sequência de números (quantidade N) e conte quantas vezes o valor 0 apareceu.
n = [23,2,0,12,329103021,3,2101,329139120]
zero = 0
for i in str(n):
    if i == '0':
        zero = zero + 1
print('Possui ', zero, 'zeros na lista')