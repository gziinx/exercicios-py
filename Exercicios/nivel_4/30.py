#  30. Peça um número N e imprima os N primeiros termos da sequência de Fibonacci (começando em 0, 1).

n = int(input("Digite um número: "))
soma = 0
num_anterior = 0
for i in range(0, n):
    num_anterior = i
    print(f"{num_anterior}")
    soma = num_anterior + 1
    print(f"{soma}")
