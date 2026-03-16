# 13. Leia 10 números e calcule a soma apenas dos positivos.

n = [11,-2,33,43,-11, 32,-12 ,54,57, -23 , 43]

j = 0
for i in n:
    if i > 0:
        j += i
        print(f"soma dos inteiros: {j}")
    else:
        print(i,"é negativo")