# 10. Peça um número e imprima a tabuada dele (1 a 10).

n = int(input("Digite a tabuada que deseja: "))
soma = 0
for i in range(1, 11):
    if i * n:
        soma += n
    print(i, "X", soma)