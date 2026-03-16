# 14. Leia um número N e calcule o somatório de 1 até N.

n = int(input("Digite um numero: "))

soma = 0

for i in range(1, n +1):
    soma = soma + i
    print(f"Numero: {i}, Soma total: {soma}")
