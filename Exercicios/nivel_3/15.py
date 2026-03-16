# 15. Leia um número N e calcule N! (fatorial) usando for (considere N >= 0).

n = int(input("Digite um numero: "))

conta = 0

for i in range(1, n -1 ):
    if  n >= 0:
        conta = n * i
print(f"{n} * {i} = {conta}")