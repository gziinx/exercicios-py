# 12. Leia 5 números e mostre o maior e o menor.

n = [11,2,33,43,11]

for i in n:
    for o in n:
        if i > o:
            print(i,"é maior que", o)
        elif i == o:
            print(i,"e ", o, "são iguais")
        else:
            print(i,"é menor que", o)
    print(" ")