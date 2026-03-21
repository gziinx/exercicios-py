# 22. Leia uma lista de N números (N informado pelo usuário) e calcule a média apenas dos números entre 0 e 100 (ignore os demais).
lista = []
bore = True
while bore:
    n = int(input("Digite o numero para a sua lista: "))
    print('----------------------')
    print ('DIGITE 00 PARA SAIR!!')
    print('----------------------')
    if n > 0 and n <=100:
        lista.append(n)
    else:
        print(' ')
        print('-----------------------------')
        print('ERRO: DIGITE NÚMEROS DE 0 e 100 !!')
        print('-----------------------------')
    if n == 00:
        bore == False
        break
    
soma = 0
for i in lista:
    soma += i
    media = soma / len(lista)

print(f"soma total: {soma}, media: {media:.2f}")