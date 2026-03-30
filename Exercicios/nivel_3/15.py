# 15. Leia um número N e calcule N! (fatorial) usando for (considere N >= 0).

n = int(input("Digite um numero: "))

fatorial = 1
for i in range(1, n + 1):
    if n > 0:
        fatorial *= i
    elif n == 0:
        print(f"O fatorial de {n} é 1")
print(f"O fatorial de {n} é {fatorial}")