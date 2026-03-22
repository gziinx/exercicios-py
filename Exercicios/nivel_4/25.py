# 25. Simule um caixa: peça o valor da compra e o valor pago. Se o pago for menor, informe saldo
# devedor. Se for maior, calcule o troco e informe quantas notas de 100, 50, 20, 10, 5, 2 e
# moedas de 1 são necessárias (use for/if para decompor).

n = int(input("Digite o valor da compra: "))
n1 = int(input("Digite o valor pago: "))
conta = n1 - n

if conta < 0:
        print(f"Ainda falta R${conta:.2f}")
elif conta == 0:
    print('Não é necessário troco')
else:
    print(f'--------------------\n TROCO \n--------------------')
for i in [1, 2, 5, 10, 20, 50, 100]:
    if conta >= i :
        if conta >= 100:
             conta = conta - 100
             print('Nota de 100') 
        if conta >= 50 and conta < 100:
             conta = conta - 50
             print('Nota de 50') 
        if conta >= 20 and conta < 50:
             conta = conta - 20
             print('Nota de 20')
        if conta >= 10 and conta < 20:
            conta = conta - 10
            print('Nota de 10') 
        if conta >= 5 and conta < 10: 
            conta = conta - 5
            print('Nota de 5') 
        if conta >= 2 and conta < 5: 
            conta = conta - 2
            print('Nota de 2')
        if conta == 1:
            conta = conta - 1
            print('Moeda de 1')