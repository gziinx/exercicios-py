# 24. Jogo simples: peça um número “secreto” (fixo no código) e dê 5 tentativas para o usuário acertar; a cada tentativa, diga se o palpite foi maior ou menor.
import random
numero_secreto = random.randint(1,100)
for i in range(5, 0, -1):
    print(f'--------------------\n VOCÊ TEM {i} TENTATIVAS \n--------------------')
    n = int(input('Digite o numero e tente acertar: '))
    if n == numero_secreto:
        print('--------------------\n VOCE GANHOU!!!')
        break
    elif n > numero_secreto:
        print(f"{n} é maior!!")
    elif n < numero_secreto:
        print(f"{n} é menor!!")
print(f'--------------------\n FIM DE JOGO \n--------------------')