# 26. Validação em loop: peça ao usuário uma nota de 0 a 10. Enquanto for inválida, peça novamente. Ao final, imprima a nota válida
while True:
    n = int(input('Digite um numero de 0 a 10: '))
    if n >= 0 and n < 11:
        print(f"{n} é a sua nota")
        break
    print('--------------\nNota invalida!!\nInsira um numero entre 0 a 10\n--------------')