# 21. Peça ao usuário um número N e imprima uma “escadinha” de asteriscos com N linhas (1 a N asteriscos).

n = int(input("Digite o numero: "))
soma = ''
for i in range(1, n + 1):
    soma += "*"
    print(i, '', soma)
   