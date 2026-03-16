# 19. Peça um número N e imprima apenas os múltiplos de 3 entre 1 e N.

n = int(input("Digite um numero: "))

for i in range(1, n +1):
    if i % 3 == 0:
        print(f"{i} é multiplo de 3" )