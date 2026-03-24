# 28. Leia um número N e verifique se ele é um número perfeito (soma dos divisores próprios = N).

n = 28
divisores = []
for i in range(1, n):
    if n % i == 0:
        divisores.append(i)
soma = 0
for i in divisores:
    soma += i

if soma == n:
    print("O seu número é perfeito")
else:
    print("Seu número não é perfeito")