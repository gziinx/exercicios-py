# 20. Leia um número inteiro e informe se ele é primo (use for para testar divisores).

n = int(input("Digite um numero: "))
divisor = 0
for i in range(1, n +1):
    if n % i == 0:
        divisor += 1

if divisor == 2:
    print("seu numero é primo")
else:
    print("seu numero não é primo")

