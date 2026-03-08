# 9. Peça um número N e imprima os números de N até 1 (ordem decrescente) usando for.

n = int(input("Digite o seu número:"))

for i in range(n, 0, -1):
    print(i)